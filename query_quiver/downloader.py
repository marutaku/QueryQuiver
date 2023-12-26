from typing import TypedDict

import requests
from bs4 import BeautifulSoup

from query_quiver.logger import create_logger


class WebPageInfo(TypedDict):
    title: str
    description: str
    keywords: list[str]


class Downloader(object):
    def __init__(self) -> None:
        self.logger = create_logger(__name__)

    def extract_information_from_webpage(self, url: str) -> WebPageInfo:
        """Extract information from webpage"""
        html = self.download_webpage(url)
        return self.parse_webpage_info(html)

    def download_webpage(self, url: str) -> str:
        """Download webpage from URL"""
        self.logger.info(f"Downloading {url}")
        response = requests.get(url)
        return response.text

    def parse_webpage_info(self, html: str) -> WebPageInfo:
        """Parse webpage info from HTML"""
        self.logger.info("Parsing webpage info")
        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string
        description = soup.find("meta", attrs={"name": "description"})
        description = description["content"] if description else ""
        keywords = soup.find("meta", attrs={"name": "keywords"})
        keywords = keywords["content"].split(",") if keywords else []
        return WebPageInfo(
            title=title,
            description=description,
            keywords=keywords,
        )
