import fire

from query_quiver.chrome_history import ChromeHistory
from query_quiver.downloader import Downloader


def generate(
    limit: int = 100, number_of_ideas: int = 10, chrome_history_path: str | None = None
):
    pass


def extract(limit: int = 100, chrome_history_path: str | None = None):
    """Generate idea of tech articles from Google Chrome history"""
    chrome_history = ChromeHistory(chrome_history_path=chrome_history_path)
    histories = chrome_history.get_history(limit=limit)
    search_words_histories = chrome_history.get_google_search_words_history(limit=limit)
    downloader = Downloader()
    webpage_infos = []
    for url, _ in histories:
        webpage_info = downloader.extract_information_from_webpage(url)
        webpage_infos.append(webpage_info)
    print(webpage_infos)
    print(search_words_histories)


def run():
    """Run the CLI"""
    fire.Fire({"generate": generate, "extract": extract})
