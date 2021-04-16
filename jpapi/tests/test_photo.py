from requests import exceptions as err
from ..photo import Photo
import pytest


class TestPhoto():

    def test_get_all_photos(self):
        try:
            photos = Photo("http://jsonplaceholder.typicode.com")
            response = photos.get()
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_get_single_photo(self):
        try:
            photos = Photo("http://jsonplaceholder.typicode.com")
            response = photos.get(5)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_add_photo(self):
        try:
            photos = Photo("http://jsonplaceholder.typicode.com")
            response = photos.add(2, 'Album Photo', 'https://fqdn/full/image.png', 'https://fqdn/thumbnail/image.png')
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 201

    def test_replace_photo(self):
        try:
            photos = Photo("http://jsonplaceholder.typicode.com")
            response = photos.replace(1, 6, 'Reaplement Photo', 'https://fqnd/full/02_image.png', 'https://fqdn/thumbnail/02_image.png')
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200
    
    def test_modify_photo(self):
        try:
            photos = Photo("http://jsonplaceholder.typicode.com")
            response = photos.modify(3, title = 'Modified Title', thumbnail = 'https://fqdn/thumbnail/03_image.png')
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200
    
    def test_delete_valid_photo(self):
        try:
            photos = Photo("http://jsonplaceholder.typicode.com")
            response = photos.delete(5)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_delete_invalid_photo(self):
        try:
            photos = Photo("http://jsonplaceholder.typicode.com")
            response = photos.delete(30000)
        except err.HTTPError:
            assert True
