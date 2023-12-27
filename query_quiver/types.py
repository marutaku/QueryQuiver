from typing import TypedDict


class WebPageInfo(TypedDict):
    title: str
    description: str
    keywords: list[str]


class ChromeKeyword(TypedDict):
    keywords: list[str]
