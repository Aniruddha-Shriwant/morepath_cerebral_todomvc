import morepath
import morepath_cerebral_todomvc
from morepath_cerebral_todomvc import App, fakedb

import json
from webtest import TestApp as Client


def setup_module(module):
    morepath.scan(morepath_cerebral_todomvc)
    morepath.commit(App)


def teardown_function(function):
    fakedb.reset_list()


def test_root():
    c = Client(App())

    response = c.get('/')
    assert response.json == {"collection": "http://localhost/todos"}


def test_list():
    c = Client(App())
    response = c.get('/todos')
    todo_list = {"todos": [
        {"@id": "http://localhost/todos/0", "title": "Code", "completed": True},
        {"@id": "http://localhost/todos/1", "title": "Test", "completed": False},
        {"@id": "http://localhost/todos/2", "title": "Document", "completed": False},
        {"@id": "http://localhost/todos/3", "title": "Release", "completed": False}
    ]}
    assert response.json == todo_list


def test_todo():
    c = Client(App())
    response = c.get('/todos/0')
    assert response.json == {"@id": "http://localhost/todos/0", "title": "Code", "completed": True}


def test_add_todo():
    c = Client(App())

    new_todo = {"@id": "http://localhost/todos/4", "title": "Something else", "completed": False}
    new_todo_json = json.dumps(new_todo)
    response = c.post('/todos', new_todo_json)
    assert response.json == new_todo


def test_delete_todo():
    c = Client(App())

    response = c.delete('/todos/2')
    todo_list = {"todos": [
        {"@id": "http://localhost/todos/0", "title": "Code", "completed": True},
        {"@id": "http://localhost/todos/1", "title": "Test", "completed": False},
        {"@id": "http://localhost/todos/3", "title": "Release", "completed": False}
    ]}
    assert response.json == todo_list


def test_change_todo():
    c = Client(App())

    changed_todo_json = json.dumps({"title": "Changed Test", "completed": True})
    response = c.put('/todos/1', changed_todo_json)
    changed_todo = {"@id": "http://localhost/todos/1", "title": "Changed Test", "completed": True}
    assert response.json == changed_todo
