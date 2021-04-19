#pylint: disable-msg=R0201,C0116

'''imports for testing'''
import pytest
import requests_mock
from requests import exceptions as err
from ..album import Album


mock_data = [
    {
        "userId": 1,
        "id": 1,
        "title": "quidem molestiae enim"
    },
    {
        "userId": 1,
        "id": 2,
        "title": "sunt qui excepturi placeat culpa"
    },
    {
        "userId": 1,
        "id": 3,
        "title": "omnis laborum odio"
    },
    {
        "userId": 1,
        "id": 4,
        "title": "non esse culpa molestiae omnis sed optio"
    }
]

class TestAlbum():
    '''Test cases for JSON Placement albums api'''
    def test_get_all_albums(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                'https://jsonplaceholder.typicode.com/albums',
                json = mock_data,
                status_code = 200
            )

            response = Album('https://jsonplaceholder.typicode.com').get()
            assert response.json() == mock_data
            assert response.status_code == 200

    def test_get_single_album(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                'https://jsonplaceholder.typicode.com/albums/1',
                json = mock_data[1],
                status_code = 200
            )

            response = Album('https://jsonplaceholder.typicode.com').get(1)
            assert response.json() == mock_data[1]
            assert response.status_code == 200

    def test_get_invalid_album(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                'https://jsonplaceholder.typicode.com/albums/500',
                status_code = 404
            )

            with pytest.raises(err.HTTPError):
                response = Album('https://jsonplaceholder.typicode.com').get(500)
                assert response.status_code == 404

    def test_add_album(self):
        with requests_mock.Mocker() as mock:
            mock.post(
                'https://jsonplaceholder.typicode.com/albums',
                headers = {'Content-Type': 'application/json'},
                status_code = 201
            )

            response = Album(
                'https://jsonplaceholder.typicode.com').add(1, 'Mock Title')
            assert response.status_code == 201

    def test_replace_album(self):
        with requests_mock.Mocker() as mock:
            mock.put(
                'https://jsonplaceholder.typicode.com/albums/1',
                headers = {'Content-Type': 'application/json'},
                status_code = 200
            )

            response = Album('https://jsonplaceholder.typicode.com') \
                .replace(1, 2, 'Mock Title')
            assert response.status_code == 200

    def test_modify_album(self):
        with requests_mock.Mocker() as mock:
            mock.patch(
                'https://jsonplaceholder.typicode.com/albums/1',
                headers = {'Content-Type': 'application/json'},
                status_code = 200
            )

            response = Album('https://jsonplaceholder.typicode.com') \
                .modify(1, title = 'Mock Title')
            assert response.status_code == 200

    def test_delete_valid_album(self):
        with requests_mock.Mocker() as mock:
            mock.delete(
                'https://jsonplaceholder.typicode.com/albums/1',
                status_code = 200
            )

            response = Album('https://jsonplaceholder.typicode.com').delete(1)
            assert response.status_code == 200

    def test_delete_invalid_album(self):
        with requests_mock.Mocker() as mock:
            mock.delete(
                'https://jsonplaceholder.typicode.com/albums/500',
                status_code = 404
            )

            with pytest.raises(err.HTTPError):
                response = Album('https://jsonplaceholder.typicode.com').delete(500)
                assert response.status_code == 404
