
from website.models import User, Task

def test_user_set_password():
    user = User()
    user.set_password('password')
    assert user.password_hash is not None
    assert user.password_hash != 'password'

def test_user_check_password():
    user = User()
    user.set_password('password')
    assert user.check_password('password')
    assert not user.check_password('wrongpassword')

def test_task_repr():
    task = Task(text='Task 1')
    assert str(task) == '<Task Task 1>'

def test_task_user():
    user = User(username='user')
    task = Task(text='Task 1', user=user)
    assert task.user == user
    assert task.user_id == user.id
    assert user.tasks == [task]