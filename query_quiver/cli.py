import fire

from query_quiver.chrome_history import ChromeHistory


def generate(
    limit: int = 100, number_of_ideas: int = 10, chrome_history_path: str = None
):
    """Generate idea of tech articles from Google Chrome history"""
    chrome_history = ChromeHistory(chrome_history_path=chrome_history_path)
    histories = chrome_history.get_history(limit=limit)
    for url, title in histories[:number_of_ideas]:
        print(f"- [{title}]({url})")


def run():
    """Run the CLI"""
    fire.Fire(
        {
            "generate": generate,
        }
    )
