#!/usr/bin/env python3
"""Convert TweetClaw exports into the training CSV used by this project."""

from __future__ import annotations

import argparse
import csv
import json
from collections.abc import Iterable, Iterator, Mapping
from pathlib import Path
from typing import Any


TEXT_FIELDS = (
    "text",
    "full_text",
    "tweet_text",
    "content",
    "body",
    "review",
    "selected_text",
)
SENTIMENT_FIELDS = ("sentiment", "label", "polarity")
VALID_SENTIMENTS = {"positive", "negative", "neutral"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert TweetClaw JSON, JSONL, NDJSON, or CSV exports to review,sentiment rows."
    )
    parser.add_argument("input", type=Path, help="TweetClaw export file")
    parser.add_argument("output", type=Path, help="CSV path to write")
    parser.add_argument(
        "--default-sentiment",
        choices=sorted(VALID_SENTIMENTS),
        default=None,
        help="Label to use when the export has no sentiment column. Review labels before training.",
    )
    return parser.parse_args()


def read_json_records(path: Path) -> Iterator[Mapping[str, Any]]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(value, list):
        yield from records_from_iterable(value)
        return
    if isinstance(value, dict):
        for key in ("tweets", "data", "items", "results"):
            nested = value.get(key)
            if isinstance(nested, list):
                yield from records_from_iterable(nested)
                return
        yield value


def read_jsonl_records(path: Path) -> Iterator[Mapping[str, Any]]:
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        value = json.loads(stripped)
        if not isinstance(value, dict):
            raise ValueError(f"Line {line_number} is not a JSON object.")
        yield value


def read_csv_records(path: Path) -> Iterator[Mapping[str, Any]]:
    with path.open(encoding="utf-8", newline="") as handle:
        yield from csv.DictReader(handle)


def records_from_iterable(values: Iterable[Any]) -> Iterator[Mapping[str, Any]]:
    for index, value in enumerate(values, start=1):
        if not isinstance(value, dict):
            raise ValueError(f"Record {index} is not an object.")
        yield value


def read_records(path: Path) -> Iterator[Mapping[str, Any]]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        yield from read_csv_records(path)
        return
    if suffix in {".jsonl", ".ndjson"}:
        yield from read_jsonl_records(path)
        return
    if suffix == ".json":
        yield from read_json_records(path)
        return
    raise ValueError("Input must be .json, .jsonl, .ndjson, or .csv.")


def nested_text(record: Mapping[str, Any]) -> str | None:
    for field in TEXT_FIELDS:
        value = record.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    for key in ("tweet", "post"):
        nested = record.get(key)
        if isinstance(nested, Mapping):
            value = nested_text(nested)
            if value:
                return value
    return None


def sentiment_for(record: Mapping[str, Any], default: str | None) -> str | None:
    for field in SENTIMENT_FIELDS:
        value = record.get(field)
        if isinstance(value, str):
            normalized = value.strip().lower()
            if normalized in VALID_SENTIMENTS:
                return normalized
    return default


def convert(input_path: Path, output_path: Path, default_sentiment: str | None) -> int:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=("review", "sentiment"))
        writer.writeheader()
        for record in read_records(input_path):
            text = nested_text(record)
            sentiment = sentiment_for(record, default_sentiment)
            if not text or sentiment is None:
                continue
            writer.writerow({"review": text, "sentiment": sentiment})
            count += 1
    return count


def main() -> None:
    args = parse_args()
    count = convert(args.input, args.output, args.default_sentiment)
    print(f"Wrote {count} training rows to {args.output}")


if __name__ == "__main__":
    main()
