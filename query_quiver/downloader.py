from typing import TypedDict

import requests
from bs4 import BeautifulSoup

from query_quiver.logger import create_logger


class WebPageInfo(TypedDict):
    title: str
    description: str
    keywords: list[str]


class Downloader(object):
    def __init__(self, client=requests) -> None:
        self.logger = create_logger(__name__)
        self.client = client

    def extract_information_from_webpage(self, url: str) -> WebPageInfo:
        """Extract information from webpage"""
        html = self.download_webpage(url)
        return self.parse_webpage_info(html)

    def download_webpage(self, url: str) -> str:
        """Download webpage from URL"""
        self.logger.info(f"Downloading {url}")
        response = self.client.get(url)
        return response.text

    def parse_webpage_info(self, html: str) -> WebPageInfo:
        """Parse webpage info from HTML

        NOTE: bs4 type hints are not correct so we ignore many type errors
        """
        self.logger.info("Parsing webpage info")
        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string or ""  # type: ignore
        description = soup.find("meta", attrs={"name": "description"})
        description_content = description["content"] if description else ""  # type: ignore
        keywords = soup.find("meta", attrs={"name": "keywords"})
        keyword_contents = keywords["content"].split(",") if keywords else []  # type: ignore
        return WebPageInfo(
            title=title,
            description=description_content
            if isinstance(description_content, str)
            else ",".join([str(d) for d in description_content]),
            keywords=keyword_contents,
        )