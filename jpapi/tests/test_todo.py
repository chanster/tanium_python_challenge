from requests import exceptions as err
from ..todo import Todo
import pytest


class TestTodo():
    
    def test_get_all_todos(self):
        try:
            todos = Todo("http://jsonplaceholder.typicode.com")
            response = todos.get()
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200
    
    def test_get_single_todo(self):
        try:
            todos = Todo("http://jsonplaceholder.typicode.com")
            response = todos.get(5)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200
    
    def test_add_todo(self):
        try:
            todos = Todo("http://jsonplaceholder.typicode.com")
            response = todos.add('My Todo Today')
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 201
    
    def test_repalce_todo(self):
        try:
            todos = Todo("http://jsonplaceholder.typicode.com")
            response = todos.replace(3, 'New Todo Title', False)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_modify_todo(self):
        try:
            todos = Todo("http://jsonplaceholder.typicode.com")
            response = todos.modify(1, completed = False)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200
    
    def test_delete_valid_todo(self):
        try:
            todos = Todo("http://jsonplaceholder.typicode.com")
            response = todos.delete(3)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_delete_invalid_todo(self):
        try:
            todos = Todo("http://jsonplaceholder.typicode.com")
            response = todos.delete(50000)
        except err.HTTPError:
            assert True
