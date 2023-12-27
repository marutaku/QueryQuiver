import os
import sqlite3
from contextlib import closing
from typing import Any
from urllib.parse import unquote

from query_quiver.types import ChromeKeyword

DEFAULT_GOOGLE_CHROME_HISTORY_SQLITE_PATH = f"/Users/{os.environ.get('USER')}/Library/Application Support/Google/Chrome/Default/History"  # noqa: E501


class ChromeHistory(object):
    def __init__(self, chrome_history_path: str | None = None) -> None:
        self.sqlite_path = (
            chrome_history_path or DEFAULT_GOOGLE_CHROME_HISTORY_SQLITE_PATH
        )

    def get_history(self, limit: int = 100) -> list:
        """Get history from Google Chrome history"""
        histories = self.fetch_data_from_chrome_history_db(
            """
            SELECT
              CASE
                WHEN INSTR(urls.url, "?") > 0 THEN SUBSTR(urls.url, 0, INSTR(urls.url, "?"))
                ELSE urls.url
              END,
              urls.title
            FROM
              visits
            LEFT OUTER JOIN
              urls
              ON
                visits.url = urls.id
            WHERE urls.url NOT LIKE 'https://www.google.com/search%'
            ORDER BY
              visits.visit_time DESC
            LIMIT ?
            """,
            (limit,),
        )
        return histories

    def get_google_search_words_history(self, limit: int = 100) -> list[ChromeKeyword]:
        """Get history from Google Chrome history"""
        histories = self.fetch_data_from_chrome_history_db(
            """
            SELECT
              urls.url
            FROM
              visits
            LEFT OUTER JOIN
              urls
              ON
                visits.url = urls.id
            WHERE urls.url LIKE 'https://www.google.com/search?%'
            ORDER BY
              visits.visit_time DESC
            LIMIT ?
            """,
            (limit,),
        )
        return [
            {
                "keywords": self.extract_chrome_query_from_url(url[0]),
            }
            for url in histories
        ]

    def extract_chrome_query_from_url(self, url: str) -> list[str]:
        """Extract query from url"""
        keywords_encoded = url.split("q=")[1].split("&")[0].replace("+", " ").split(" ")
        return [unquote(keyword) for keyword in keywords_encoded]

    def fetch_data_from_chrome_history_db(
        self, query: str, params: tuple[Any, ...]
    ) -> list:
        """Execute SQL query"""
        with closing(sqlite3.connect(self.sqlite_path, timeout=5)) as conn:
            c = conn.cursor()
            c.execute(query, params)
            return c.fetchall()
