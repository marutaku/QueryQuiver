import fire

from query_quiver.chrome_history import ChromeHistory
from query_quiver.downloader import Downloader
from query_quiver.generator import ArticleIdeaGenerator


def generate(
    limit: int = 100,
    number_of_ideas: int = 10,
    chrome_history_path: str | None = None,
    openai_api_key: str | None = None,
):
    """Generate idea of tech articles from Google Chrome history"""
    chrome_history = ChromeHistory(chrome_history_path=chrome_history_path)
    downloader = Downloader()
    generator = ArticleIdeaGenerator(openai_api_key=openai_api_key)
    histories = chrome_history.get_history(limit=limit)
    search_words_histories = chrome_history.get_google_search_words_history(limit=limit)
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
