import os
import sqlite3
from contextlib import closing

DEFAULT_GOOGLE_CHROME_HISTORY_SQLITE_PATH = f"/Users/{os.environ.get('USER')}/Library/Application Support/Google/Chrome/Default/History"  # noqa: E501


class ChromeHistory(object):
    def __init__(self, chrome_history_path: str | None = None) -> None:
        self.sqlite_path = (
            chrome_history_path or DEFAULT_GOOGLE_CHROME_HISTORY_SQLITE_PATH
        )

    def get_history(self, limit: int = 100) -> list:
        """Get history from Google Chrome history"""
        with closing(sqlite3.connect(self.sqlite_path)) as conn:
            c = conn.cursor()
            c.execute(
                """
                SELECT
                  DISTINCT
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
            history = c.fetchall()
            return history
