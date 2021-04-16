from requests import exceptions as err
from ..user import User
import pytest


class TestUser:

    def test_get_all_users(self):
        try:
            users = User("http://jsonplaceholder.typicode.com")
            response = users.get()
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200
    
    def test_get_single_user(self):
        try:
            users = User("http://jsonplaceholder.typicode.com")
            response = users.get(4)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200
    
    def test_add_user(self):
        try:
            users = User("http://jsonplaceholder.typicode.com")
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
            response = users.add(
                            content['name'],
                            content['username'],
                            content['email'],
                            content['address'],
                            content['phone'],
                            content['website'],
                            content['company']
                       )
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 201

    def test_replace_user(self):
        try:
            users = User("http://jsonplaceholder.typicode.com")
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
            response = users.replace(2,
                            content['name'],
                            content['username'],
                            content['email'],
                            content['address'],
                            content['phone'],
                            content['website'],
                            content['company']
                      )
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_modify_user(self):
        try:
            users = User("http://jsonplaceholder.typicode.com")
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
            response = users.modify(1)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200
    
    def test_delete_valid_user(self):
        try:
            users = User("http://jsonplaceholder.typicode.com")
            response = users.delete(2)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200
    
    def test_delete_invalid_user(self):
        try:
            users = User("http://jsonplaceholder.typicode.com")
            response = users.delete(200)
        except err.HTTPError:
            assert True
