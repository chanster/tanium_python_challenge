#pylint: disable-msg=R0201,C0116

'''imports for testing'''
import pytest
import requests_mock
from requests import exceptions as err
from ..photo import Photo

mock_data = [
    {
        "albumId": 1,
        "id": 1,
        "title": "accusamus beatae ad facilis cum similique qui sunt",
        "url": "https://via.placeholder.com/600/92c952",
        "thumbnailUrl": "https://via.placeholder.com/150/92c952"
    },
    {
        "albumId": 1,
        "id": 2,
        "title": "reprehenderit est deserunt velit ipsam",
        "url": "https://via.placeholder.com/600/771796",
        "thumbnailUrl": "https://via.placeholder.com/150/771796"
    },
    {
        "albumId": 1,
        "id": 3,
        "title": "officia porro iure quia iusto qui ipsa ut modi",
        "url": "https://via.placeholder.com/600/24f355",
        "thumbnailUrl": "https://via.placeholder.com/150/24f355"
    },
    {
        "albumId": 1,
        "id": 4,
        "title": "culpa odio esse rerum omnis laboriosam voluptate repudiandae",
        "url": "https://via.placeholder.com/600/d32776",
        "thumbnailUrl": "https://via.placeholder.com/150/d32776"
    },
    {
        "albumId": 1,
        "id": 5,
        "title": "natus nisi omnis corporis facere molestiae rerum in",
        "url": "https://via.placeholder.com/600/f66b97",
        "thumbnailUrl": "https://via.placeholder.com/150/f66b97"
    }
]

class TestPhoto():
    '''Test cases for JSON Placement photos api'''
    def test_get_all_photos(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                'https://jsonplaceholder.typicode.com/photos',
                json = mock_data,
                status_code = 200
            )

            response = Photo('https://jsonplaceholder.typicode.com').get()
            assert response.json() == mock_data
            assert response.status_code == 200

    def test_get_single_photo(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                'https://jsonplaceholder.typicode.com/photos/1',
                json = mock_data[1],
                status_code = 200
            )

            response = Photo('https://jsonplaceholder.typicode.com').get(1)
            assert response.json() == mock_data[1]
            assert response.status_code == 200

    def test_add_photo(self):
        with requests_mock.Mocker() as mock:
            mock.post(
                'https://jsonplaceholder.typicode.com/photos',
                headers = {'Content-Type': 'application/json'},
                status_code = 201
            )

            response = Photo('https://jsonplaceholder.typicode.com') \
                .add(
                    2,
                    'Mock Title',
                    'http://mock/full/image.png',
                    'http://mock/thumbnail/image.png'
                )
            assert response.status_code == 201

    def test_replace_photo(self):
        with requests_mock.Mocker() as mock:
            mock.put(
                'https://jsonplaceholder.typicode.com/photos/2',
                headers = {'Content-Type': 'application/json'},
                status_code = 200
            )

            response = Photo('https://jsonplaceholder.typicode.com') \
                .replace(
                    2,
                    3,
                    'Mock Title',
                    'http://mock/full/image.png',
                    'http://mock/thumbnail/image.png'
                )
            assert response.status_code == 200

    def test_modify_photo(self):
        with requests_mock.Mocker() as mock:
            mock.patch(
                'https://jsonplaceholder.typicode.com/photos/2',
                headers = {'Content-Type': 'application/json'},
                status_code = 200
            )

            response = Photo('https://jsonplaceholder.typicode.com') \
                .modify(
                    2,
                    title = 'Mock Title',
                    thumbnail = 'http://mock/thumbnail/image02.png'
                )
            assert response.status_code == 200

    def test_delete_valid_photo(self):
        with requests_mock.Mocker() as mock:
            mock.delete(
                'https://jsonplaceholder.typicode.com/photos/1',
                status_code = 200
            )

            response = Photo('https://jsonplaceholder.typicode.com').delete(1)
            assert response.status_code == 200

    def test_delete_invalid_photo(self):
        with requests_mock.Mocker() as mock:
            mock.delete(
                'https://jsonplaceholder.typicode.com/photos/500',
                status_code = 404
            )

            with pytest.raises(err.HTTPError):
                response = Photo('https://jsonplaceholder.typicode.com').delete(500)
                assert response.status_code == 404
