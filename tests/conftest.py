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


@pytest.fixture(scope='module')
def init_database(test_client):

    test_client.post('/signup', data=dict(username='test', password='test'), follow_redirects=True)

    yield # this is where the testing happens!

    # Delete the user after the tests run
    with test_client.application.app_context():
        db.drop_all()


@pytest.fixture(scope='module')
def login_user(test_client, init_database):
    test_client.post('/login', data=dict(username='test', password='test'), follow_redirects=True)

    yield

    test_client.get('/logout', follow_redirects=True)

####################
#  Google auth idea
####################

# Mocking the flow object for testing
class MockFlow:
    def authorization_url(self):
        return "http://example.com/auth", "mock_state"
    

@pytest.fixture(scope='module')
def google_client():
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    flask_app.blueprints['auth'].flow = MockFlow()

    with flask_app.test_client() as test_client:
        yield test_client


def test_login_redirect(google_client):

    # Test the login-g route
    response = google_client.get('/login-g')

    # Check the response is a redirect
    assert response.status_code == 302

    # Check the redirect location is correct
    assert response.headers['Location'] == "http://example.com/auth"

    # Check the state is stored in the session
    with google_client.session_transaction() as session:
        assert session['state'] == "mock_state"