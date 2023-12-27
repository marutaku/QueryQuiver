import logging

import fire

from query_quiver.chrome_history import ChromeHistory
from query_quiver.downloader import Downloader
from query_quiver.generator import ArticleIdeaGenerator


def setup_logging(debug: bool = False):
    """Setup logging"""
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)


def generate(
    query_history_limit: int = 20,
    number_of_ideas: int = 5,
    chrome_history_path: str | None = None,
    openai_api_key: str | None = None,
    debug: bool = False,
):
    """Generate idea of tech articles from Google Chrome history"""
    setup_logging(debug)
    chrome_history = ChromeHistory(chrome_history_path)
    downloader = Downloader()
    generator = ArticleIdeaGenerator(openai_api_key)
    histories = chrome_history.get_history(limit=query_history_limit)
    search_words_histories = chrome_history.get_google_search_words_history(
        limit=query_history_limit
    )
    webpage_infos = []
    for url, _ in histories:
        webpage_info = downloader.extract_information_from_webpage(url)
        webpage_infos.append(webpage_info)
    print(
        generator.generate_ideas(
            chrome_visit_site_history=webpage_infos,
            chrome_search_words_history=search_words_histories,
            number_of_ideas=number_of_ideas,
        )
    )


def run():
    """Run the CLI"""
    fire.Fire({"generate": generate})
