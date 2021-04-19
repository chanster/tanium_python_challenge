from requests import exceptions as err
from ..todo import Todo
import pytest
import requests_mock


mock_data = [
    {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    },
    {
        "userId": 1,
        "id": 2,
        "title": "quis ut nam facilis et officia qui",
        "completed": False
    },
    {
        "userId": 1,
        "id": 3,
        "title": "fugiat veniam minus",
        "completed": False
    },
    {
        "userId": 1,
        "id": 4,
        "title": "et porro tempora",
        "completed": True
    },
    {
        "userId": 1,
        "id": 5,
        "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
        "completed": False
    },
    {
        "userId": 1,
        "id": 6,
        "title": "qui ullam ratione quibusdam voluptatem quia omnis",
        "completed": False
    }
]

class TestTodo():
    
    def test_get_all_todos(self):
        with requests_mock.Mocker() as mock:
            mock.get('https://jsonplaceholder.typicode.com/todos', json = mock_data, status_code = 200)

            response = Todo('https://jsonplaceholder.typicode.com').get()
            assert response.json() == mock_data
            assert response.status_code == 200
    
    def test_get_single_todo(self):
        with requests_mock.Mocker() as mock:
            mock.get('https://jsonplaceholder.typicode.com/todos/1', json = mock_data[1], status_code = 200)

            response = Todo('https://jsonplaceholder.typicode.com').get(1)
            assert response.json() == mock_data[1]
            assert response.status_code == 200
    
    def test_add_todo(self):
        with requests_mock.Mocker() as mock:
            mock.post(
                'https://jsonplaceholder.typicode.com/todos',
                headers = {'Content-Type': 'application/json'},
                status_code = 201
            )

            response = Todo('https://jsonplaceholder.typicode.com') \
                .add(1, 'Mock todo')
            assert response.status_code == 201
    
    def test_repalce_todo(self):
        with requests_mock.Mocker() as mock:
            mock.put(
                'https://jsonplaceholder.typicode.com/todos/1',
                headers = {'Content-Type': 'application/json'},
                status_code = 200
            )

            response = Todo('https://jsonplaceholder.typicode.com') \
                .replace(1, 1, 'Mock todo', True)
            assert response.status_code == 200

    def test_modify_todo(self):
        with requests_mock.Mocker() as mock:
            mock.patch(
                'https://jsonplaceholder.typicode.com/todos/1',
                headers = {'Content-Type': 'application/json'},
                status_code = 200
            )

            response = Todo('https://jsonplaceholder.typicode.com') \
                .modify(1, completed = False)
            assert response.status_code == 200
    
    def test_delete_valid_todo(self):
        with requests_mock.Mocker() as mock:
            mock.delete(
                'https://jsonplaceholder.typicode.com/todos/1',
                status_code = 200
            )

            response = Todo('https://jsonplaceholder.typicode.com').delete(1)
            assert response.status_code == 200

    def test_delete_invalid_todo(self):
        with requests_mock.Mocker() as mock:
            mock.delete(
                'https://jsonplaceholder.typicode.com/todos/500',
                status_code = 404
            )

            with pytest.raises(err.HTTPError):
                response = Todo('https://jsonplaceholder.typicode.com').delete(500)
                assert response.status_code == 404
