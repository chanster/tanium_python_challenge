#pylint: disable-msg=R0201,C0116

'''imports for testing'''
import pytest
import requests_mock
from requests import exceptions as err
from ..post import Post


mock_data = [
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    },
    {
        "userId": 1,
        "id": 2,
        "title": "qui est esse",
        "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    },
    {
        "userId": 1,
        "id": 3,
        "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
        "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
    },
    {
        "userId": 1,
        "id": 4,
        "title": "eum et est occaecati",
        "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
    },
    {
        "userId": 1,
        "id": 5,
        "title": "nesciunt quas odio",
        "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
    }
]

class TestPost():
    '''Test cases for JSON Placement posts api'''
    def test_get_all_posts(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                'https://jsonplaceholder.typicode.com/posts',
                json = mock_data,
                status_code = 200
            )

            response = Post('https://jsonplaceholder.typicode.com').get()
            assert response.json() == mock_data
            assert response.status_code == 200

    def test_get_single_post(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                'https://jsonplaceholder.typicode.com/posts/1',
                json = mock_data[1],
                status_code = 200
            )

            response = Post('https://jsonplaceholder.typicode.com').get(1)
            assert response.json() == mock_data[1]
            assert response.status_code == 200

    def test_add_post(self):
        with requests_mock.Mocker() as mock:
            mock.post(
                'https://jsonplaceholder.typicode.com/posts',
                headers = {'Content-Type': 'application/json'},
                status_code = 201
            )

            response = Post('https://jsonplaceholder.typicode.com') \
                .add(2, 'Mock Title', 'Mock body.')
            assert response.status_code == 201

    def test_replace_post(self):
        with requests_mock.Mocker() as mock:
            mock.put(
                'https://jsonplaceholder.typicode.com/posts/2',
                headers = {'Content-Type': 'application/json'},
                status_code = 200
            )

            response = Post('https://jsonplaceholder.typicode.com') \
                .replace(2, 3, 'Mock Replace Title', 'Mock replace body.')
            assert response.status_code == 200

    def test_modify_post(self):
        with requests_mock.Mocker() as mock:
            mock.patch(
                'https://jsonplaceholder.typicode.com/posts/3',
                headers = {'Content-Type': 'application/json'},
                status_code = 200
            )

            response = Post('https://jsonplaceholder.typicode.com') \
                .modify(3, title = 'Mock Modify Title')
            assert response.status_code == 200

    def test_delete_valid_post(self):
        with requests_mock.Mocker() as mock:
            mock.delete(
                'https://jsonplaceholder.typicode.com/posts/1',
                status_code = 200
            )

            response = Post('https://jsonplaceholder.typicode.com').delete(1)
            assert response.status_code == 200

    def test_delete_invalid_post(self):
        with requests_mock.Mocker() as mock:
            mock.delete(
                'https://jsonplaceholder.typicode.com/posts/500',
                status_code = 404
            )

            with pytest.raises(err.HTTPError):
                response = Post('https://jsonplaceholder.typicode.com').delete(500)
                assert response.status_code == 404
