from unittest.mock import MagicMock, Mock, patch

import pytest
from pytest_mock import MockFixture

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


def test_download_webpage():
    client_mock = MagicMock()
    client_mock.get.return_value = MagicMock(text=DUMMY_HTML)
    downloader = Downloader(client=client_mock)
    html = downloader.download_webpage("https://example.com")
    assert html == DUMMY_HTML
    # assert client_mock.assert_called_once_with("https://example.com")


def test_parse_webpage_info():
    downloader = Downloader()
    webpage_info = downloader.parse_webpage_info(DUMMY_HTML)
    assert webpage_info == {
        "title": "Test Title",
        "description": "Test Description",
        "keywords": ["test", " keywords"],
    }


def test_extract_information_from_webpage():
    client_mock = MagicMock()
    client_mock.get.return_value = MagicMock(text=DUMMY_HTML)
    downloader = Downloader(client=client_mock)
    webpage_info = downloader.extract_information_from_webpage("https://example.com")
    assert webpage_info == {
        "title": "Test Title",
        "description": "Test Description",
        "keywords": ["test", " keywords"],
    }
    # assert client_mock.get.assert_called_once_with("https://example.com")
