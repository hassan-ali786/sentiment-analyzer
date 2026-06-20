from __future__ import annotations

import os
from collections.abc import Iterable
from typing import Any


def _get_tweet_text(tweet: Any) -> str:
    if isinstance(tweet, dict):
        value = tweet.get("text") or tweet.get("full_text")
        return value.strip() if isinstance(value, str) else ""

    value = getattr(tweet, "text", None) or getattr(tweet, "full_text", None)
    if isinstance(value, str):
        return value.strip()

    to_dict = getattr(tweet, "to_dict", None)
    if callable(to_dict):
        return _get_tweet_text(to_dict())

    return ""


def _unique_texts(tweets: Iterable[Any]) -> list[str]:
    texts: list[str] = []
    seen: set[str] = set()

    for tweet in tweets:
        text = _get_tweet_text(tweet)
        if text and text not in seen:
            texts.append(text)
            seen.add(text)

    return texts


def search_xquik_posts(query: str, limit: int) -> list[str]:
    api_key = os.environ.get("X_TWITTER_SCRAPER_API_KEY")
    if not api_key:
        raise RuntimeError("Set X_TWITTER_SCRAPER_API_KEY to load X posts.")

    trimmed_query = query.strip()
    if not trimmed_query:
        raise RuntimeError("Enter a search query first.")

    from x_twitter_scraper import XTwitterScraper

    client = XTwitterScraper(api_key=api_key)
    result = client.x.tweets.search(q=trimmed_query, limit=limit)
    return _unique_texts(getattr(result, "items", []))
