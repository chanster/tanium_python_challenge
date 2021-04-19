#pylint: disable-msg=R0201

'''imports for testing'''
import pytest
import requests_mock
from requests import exceptions as err
from ..user import User


mock_data = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets"
        }
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv",
        "address": {
        "street": "Victor Plains",
        "suite": "Suite 879",
        "city": "Wisokyburgh",
        "zipcode": "90566-7771",
        "geo": {
            "lat": "-43.9509",
            "lng": "-34.4618"
        }
        },
        "phone": "010-692-6593 x09125",
        "website": "anastasia.net",
        "company": {
        "name": "Deckow-Crist",
        "catchPhrase": "Proactive didactic contingency",
        "bs": "synergize scalable supply-chains"
        }
    },
    {
        "id": 3,
        "name": "Clementine Bauch",
        "username": "Samantha",
        "email": "Nathan@yesenia.net",
        "address": {
        "street": "Douglas Extension",
        "suite": "Suite 847",
        "city": "McKenziehaven",
        "zipcode": "59590-4157",
        "geo": {
            "lat": "-68.6102",
            "lng": "-47.0653"
        }
        },
        "phone": "1-463-123-4447",
        "website": "ramiro.info",
        "company": {
        "name": "Romaguera-Jacobson",
        "catchPhrase": "Face to face bifurcated interface",
        "bs": "e-enable strategic applications"
        }
    }
]

class TestUser:
    '''Test cases for JSON Placement users api'''
    def test_get_all_users(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                'https://jsonplaceholder.typicode.com/users',
                json = mock_data,
                status_code = 200
            )

            response = User('https://jsonplaceholder.typicode.com').get()
            assert response.json() == mock_data
            assert response.status_code == 200

    def test_get_single_user(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                'https://jsonplaceholder.typicode.com/users/1',
                json = mock_data[1],
                status_code = 200
            )

            response = User('https://jsonplaceholder.typicode.com').get(1)
            assert response.json() == mock_data[1]
            assert response.status_code == 200

    def test_get_single_user_albums(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                'https://jsonplaceholder.typicode.com/users/1/albums',
                status_code = 200
            )

            response = User('https://jsonplaceholder.typicode.com').get_albums(1)
            assert response.status_code == 200

    def test_get_single_user_todos(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                'https://jsonplaceholder.typicode.com/users/1/todos',
                status_code = 200
            )

            response = User('https://jsonplaceholder.typicode.com').get_todos(1)
            assert response.status_code == 200

    def test_get_single_user_posts(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                'https://jsonplaceholder.typicode.com/users/1/posts',
                status_code = 200
            )

            response = User('https://jsonplaceholder.typicode.com').get_posts(1)
            assert response.status_code == 200

    def test_add_user(self):
        with requests_mock.Mocker() as mock:
            mock.post(
                'https://jsonplaceholder.typicode.com/users',
                headers = {'Content-Type': 'application/json'},
                status_code = 201,
            )

            content = {
                'name': 'Link Dude',
                'username': 'link',
                'email': 'link@hyrule.nil',
                'address': {
                    'street': '123 Street',
                    'suite': 'Apt. 2',
                    'city': 'Hyrule',
                    'zipcode': '11111-2222',
                    'geo': {
                        'lat': '0.0',
                        'lng': '0.0'
                    }
                },
                'phone': '1-555-555-5555',
                'website': 'nintendo.com',
                'company': {
                    'name': 'Twilight',
                    'catchPhrase': 'Hey Listen',
                    'bs': 'Ha Hiya'
                }
            }

            response = User('https://jsonplaceholder.typicode.com') \
                .add(
                    content['name'],
                    content['username'],
                    content['email'],
                    content['address'],
                    content['phone'],
                    content['website'],
                    content['company']
                )
            assert response.status_code == 201

    def test_replace_user(self):
        with requests_mock.Mocker() as mock:
            mock.put(
                'https://jsonplaceholder.typicode.com/users/2',
                headers = {'Content-Type': 'application/json'},
                status_code = 200,
            )

            content = {
                'name': 'Ganon Dude',
                'username': 'ganon',
                'email': 'ganon@hyrule.nil',
                'address': {
                    'street': '123 Tutrle Rock',
                    'suite': 'Apt. 10',
                    'city': 'Hyrule',
                    'zipcode': '99999-2222',
                    'geo': {
                        'lat': '100.0',
                        'lng': '-100.0'
                    }
                },
                'phone': '1-999-555-5555',
                'website': 'nintendo.com',
                'company': {
                    'name': 'Evil',
                    'catchPhrase': 'Horseback all day',
                    'bs': 'Hahaha'
                }
            }

            response = User('https://jsonplaceholder.typicode.com') \
                .replace(2,
                    content['name'],
                    content['username'],
                    content['email'],
                    content['address'],
                    content['phone'],
                    content['website'],
                    content['company']
                )
            assert response.status_code == 200

    def test_modify_user(self):
        with requests_mock.Mocker() as mock:
            mock.patch(
                'https://jsonplaceholder.typicode.com/users/1',
                headers = {'Content-Type': 'application/json'},
                status_code = 200,
            )

            content = {
                'name': 'Zelda Dudette',
                'username': 'zelda',
                'address': {
                    'geo': {
                        'lat': '200.0',
                        'lng': '500.0'
                    }
                },
                'phone': '1-999-555-5555',
                'company': {
                    'catchPhrase': 'It\'s a secret to everybody',
                }
            }
            response = User('https://jsonplaceholder.typicode.com') \
                .modify(
                    1,
                    name = content['name'],
                    username = content['username'],
                    address = content['address'],
                    phone = content['phone'],
                    company = content['company']
                )
            assert response.status_code == 200

    def test_delete_valid_user(self):
        with requests_mock.Mocker() as mock:
            mock.delete(
                'https://jsonplaceholder.typicode.com/users/1',
                status_code = 200
            )

            response = User('https://jsonplaceholder.typicode.com').delete(1)
            assert response.status_code == 200

    def test_delete_invalid_user(self):
        with requests_mock.Mocker() as mock:
            mock.delete(
                'https://jsonplaceholder.typicode.com/users/500',
                status_code = 404
            )

            with pytest.raises(err.HTTPError):
                response = User('https://jsonplaceholder.typicode.com').delete(500)
                assert response.status_code == 404
