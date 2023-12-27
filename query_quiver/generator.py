import os

import openai

from query_quiver.logger import create_logger
from query_quiver.prompt import IDEA_GENERATE_SYSTEM_PROMPT, IDEA_GENERATE_USER_PROMPT
from query_quiver.types import ChromeKeyword, WebPageInfo


class ArticleIdeaGenerator(object):
    def __init__(self, openai_api_key: str | None = None) -> None:
        self.logger = create_logger(__name__)
        self.openai_client = openai.Client(
            api_key=openai_api_key or os.environ["OPENAI_API_KEY"]
        )

    def generate_ideas(
        self,
        chrome_visit_site_history: list[WebPageInfo],
        chrome_search_words_history: list[ChromeKeyword],
        number_of_ideas: int = 5,
    ):
        """Generate ideas of tech articles"""
        chrome_visit_site_history_str = "\n\n".join(
            [str(chrome_visit_site) for chrome_visit_site in chrome_visit_site_history]
        )
        chrome_search_words_history_str = "\n".join(
            [
                str(chrome_search_words)
                for chrome_search_words in chrome_search_words_history
            ]
        )
        result = self.call_llm_api(
            IDEA_GENERATE_SYSTEM_PROMPT.format(number_of_ideas=number_of_ideas),
            IDEA_GENERATE_USER_PROMPT.format(
                visit_site_history=chrome_visit_site_history_str,
                search_words_history=chrome_search_words_history_str,
            ),
        )
        return result

    def call_llm_api(self, system_prompt: str, user_prompt: str) -> str:
        self.logger.debug("Calling LLM API")
        self.logger.debug(f"system_prompt: {system_prompt}, user_prompt: {user_prompt}")
        response = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.choices[0].message.content or ""
