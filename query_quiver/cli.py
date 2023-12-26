import fire

from query_quiver.chrome_history import ChromeHistory
from query_quiver.downloader import Downloader


def generate(
    limit: int = 100, number_of_ideas: int = 10, chrome_history_path: str | None = None
):
    """Generate idea of tech articles from Google Chrome history"""
    chrome_history = ChromeHistory(chrome_history_path=chrome_history_path)
    histories = chrome_history.get_history(limit=limit)
    downloader = Downloader()
    for url, _ in histories[:number_of_ideas]:
        webpage_info = downloader.extract_information_from_webpage(url)
        print(f"{url}: {webpage_info}")


def run():
    """Run the CLI"""
    fire.Fire(
        {
            "generate": generate,
        }
    )
