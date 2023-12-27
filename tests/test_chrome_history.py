from unittest.mock import patch

import pytest

from query_quiver.chrome_history import ChromeHistory


@pytest.fixture
def chrome_history():
    return ChromeHistory()


def test_get_history(chrome_history: ChromeHistory):
    dummy_histories = [
        ["https://www.example1.com", "Example1"],
        ["https://www.example2.com", "Example2"],
        ["https://www.example3.com", "Example3"],
        ["https://www.example4.com", "Example4"],
        ["https://www.example5.com", "Example5"],
    ]
    with patch.object(chrome_history, "fetch_data_from_chrome_history_db") as mock:
        mock.return_value = dummy_histories
        histories = chrome_history.get_history()
        assert histories == dummy_histories
        mock.assert_called_once()


def test_get_google_search_words_history(chrome_history: ChromeHistory):
    dummy_histories = [
        ["https://www.google.com/search?q=example1"],
        ["https://www.google.com/search?q=example2"],
        ["https://www.google.com/search?q=example3"],
        ["https://www.google.com/search?q=example4"],
        ["https://www.google.com/search?q=example5"],
    ]
    with patch.object(chrome_history, "fetch_data_from_chrome_history_db") as mock:
        mock.return_value = dummy_histories
        histories = chrome_history.get_google_search_words_history()
        assert histories == [
            {"keywords": ["example1"]},
            {"keywords": ["example2"]},
            {"keywords": ["example3"]},
            {"keywords": ["example4"]},
            {"keywords": ["example5"]},
        ]
        mock.assert_called_once()
