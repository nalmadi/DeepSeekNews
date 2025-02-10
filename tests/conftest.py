import pytest
from website import create_app, db
from flask import session
import os

@pytest.fixture(scope='module')
def test_client():
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        yield test_client # this is where the testing happens!


def test_get_articles():

    articles = [{'source': {'id': None, 'name': 'Yahoo Entertainment'},
                'author': 'Steve Dent',
                'title': 'China’s DeepSeek AI assistant becomes top free iPhone app as US tech stocks take a hit',
                'description': "Chinese AI assistant DeepSeek has become the top rated free app on Apple's App Store in the US and elsewhere, beating out ChatGPT and other rivals. It's powered by the open-source DeepSeek V3 model, which reportedly requires far less computing power than comp…",
                'url': 'https://consent.yahoo.com/v2/collectConsent?sessionId=1_cc-session_77718621-45d9-4bdb-8512-cebc2edfb974',
                'urlToImage': None,
                'publishedAt': '2025-01-27T13:44:45Z',
                'content': "If you click 'Accept all', we and our partners, including 239 who are part of the IAB Transparency &amp; Consent Framework, will also store and/or access information on a device (in other words, use … [+703 chars]"}]

    return articles

@pytest.fixture(scope='function')
def news_api_mock_client(mocker):
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # need to pip install pytest-mock for mocker to work
    mocker.patch('website.views.get_articles', test_get_articles) 

    with flask_app.test_client() as test_client:
        yield test_client
