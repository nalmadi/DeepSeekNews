

def test_home_page_mock_api(news_api_mock_client):
    """
    GIVEN a Flask application configured for testing, without 
    WHEN the '/' page is requested (GET)
    THEN check the response is valid and contains the expected text
    """
    response = news_api_mock_client.get('/', follow_redirects=True)

    assert response.status_code == 200
    assert b'DeepSeek AI assistant' in response.data
    assert b'Yahoo Entertainment' in response.data
    assert b'has become the top rated free app' in response.data