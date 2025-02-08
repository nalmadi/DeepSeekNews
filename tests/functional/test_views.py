

def test_home_page_without_login(test_client):
    """
    GIVEN a Flask application configured for testing, user not logged in
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'name' in response.data
    assert b'password' in response.data


def test_home_page_with_login(test_client, login_user):
    """
    GIVEN a Flask application configured for testing, user logged in
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/', follow_redirects=True)
    assert response.status_code == 200
    assert b'To-Do List' in response.data
    assert b'Add Task' in response.data
    assert b'Add a new task' in response.data


def test_add_task(test_client, login_user):
    """
    GIVEN a Flask application configured for testing, user logged in
    WHEN the '/add' page is posted to (POST) with a new task
    THEN check the response is valid
    """
    response = test_client.post('/', data=dict(task='Test Task'), follow_redirects=True)
    assert response.status_code == 200
    assert b'To-Do List' in response.data
    assert b'Add Task' in response.data
    assert b'Add a new task' in response.data
    assert b'Test Task' in response.data
    assert b'not-completed' in response.data


def test_check_task(test_client, login_user):
    """
    GIVEN a Flask application configured for testing, user logged in
    WHEN the '/check/<int:task_id>' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/check/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'To-Do List' in response.data
    assert b'Add Task' in response.data
    assert b'Add a new task' in response.data
    assert b'completed' in response.data

def test_check_task_not_owner(test_client, login_user):
    """
    GIVEN a Flask application configured for testing, user logged in
    WHEN the '/check/<int:task_id>' page is requested (GET) for a task not owned by the user
    THEN check the response is valid
    """
    response = test_client.get('/check/2', follow_redirects=True)
    assert response.status_code == 200
    assert b'To-Do List' in response.data
    assert b'Add Task' in response.data
    assert b'Add a new task' in response.data