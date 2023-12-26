from unittest.mock import MagicMock

import pytest

from query_quiver.downloader import Downloader

DUMMY_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Test Title</title>
    <meta name="description" content="Test Description">
    <meta name="keywords" content="test, keywords">
</head>
<body>
    <h1>Test Title</h1>
    <p>Test Description</p>
    <p>Test Keywords</p>
</body>
</html>
"""

DUMMY_URL = "https://example.com"


@pytest.fixture
def mock_client():
    client_mock = MagicMock()
    client_mock.get.return_value = MagicMock(text=DUMMY_HTML)
    return client_mock


def test_download_webpage(mock_client):
    client_mock = MagicMock()
    client_mock.get.return_value = MagicMock(text=DUMMY_HTML)
    downloader = Downloader(client=mock_client)
    html = downloader.download_webpage("https://example.com")
    mock_client.get.assert_called_once_with("https://example.com")
    assert html == DUMMY_HTML


def test_parse_webpage_info():
    downloader = Downloader()
    webpage_info = downloader.parse_webpage_info(DUMMY_HTML)
    assert webpage_info == {
        "title": "Test Title",
        "description": "Test Description",
        "keywords": ["test", " keywords"],
    }


def test_extract_information_from_webpage(mock_client):
    client_mock = MagicMock()
    client_mock.get.return_value = MagicMock(text=DUMMY_HTML)
    downloader = Downloader(client=mock_client)
    webpage_info = downloader.extract_information_from_webpage("https://example.com")
    mock_client.get.assert_called_once_with("https://example.com")
    assert webpage_info == {
        "title": "Test Title",
        "description": "Test Description",
        "keywords": ["test", " keywords"],
    }
