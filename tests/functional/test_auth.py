
from website import create_app
import os

def test_login_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    # # Set the Testing configuration prior to creating the Flask application
    # os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    # flask_app = create_app()

    # # Create a test client using the Flask application configured for testing
    # with flask_app.test_client() as test_client:
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'name' in response.data
    assert b'password' in response.data


def test_signup_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/signup' page is requested (GET)
    THEN check the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/signup')
        assert response.status_code == 200
        assert b'Sign-up' in response.data
        assert b'name' in response.data
        assert b'password' in response.data


def test_failed_login(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST) with incorrect credentials
    THEN check the response is valid
    """
    response = test_client.post('/login', data=dict(username='admin', password='wrongpassword'))
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'name' in response.data
    assert b'password' in response.data
    #assert b'Invalid username or password' in response.data


def test_signup(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/signup' page is posted to (POST) with correct credentials
    THEN check the response is valid
    """
    response = test_client.post('/signup', data=dict(username='test22', password='test22'), follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'name' in response.data
    assert b'password' in response.data


def test_successful_login(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST) with correct credentials
    THEN check the response is valid
    """
    response = test_client.post('/login', data=dict(username='test', password='test'), follow_redirects=True)
    assert response.status_code == 200
    assert b'To-Do List' in response.data
    #assert b'Logout' in response.data


def test_wrong_password_login(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST) with wrong password
    THEN check the response is valid
    """
    response = test_client.post('/login', data=dict(username='test', password='wrongpassword'))
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'name' in response.data
    assert b'password' in response.data
    #assert b'Invalid username or password' in response.data


def test_logout(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'name' in response.data
    assert b'password' in response.data


def test_signup_existing_user(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/signup' page is posted to (POST) with existing user
    THEN check the response is valid
    """
    response = test_client.post('/signup', data=dict(username='test', password='test'), follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'name' in response.data
    assert b'password' in response.data