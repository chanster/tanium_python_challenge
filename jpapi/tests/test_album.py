from requests import exceptions as err
from ..album import Album
import pytest


class TestAlbum():

    def test_get_all_albums(self):
        try:
            albums = Album("http://jsonplaceholder.typicode.com")
            response = albums.get()
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_get_single_album(self):
        try:
            albums = Album("http://jsonplaceholder.typicode.com")
            response = albums.get(5)
        except err.HTTPError():
            assert False
        finally:
            assert response.status_code == 200
    
    def test_get_invalid_album(self):
        try:
            albums = Album("http://jsonplaceholder.typicode.com")
            response = albums.get(500)
        except err.HTTPError():
            assert True

    def test_add_album(self):
        try:
            albums = Album("http://jsonplaceholder.typicode.com")
            response = albums.add(1, 'Test album title')
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 201
    
    def test_replace_album(self):
        try:
            albums = Album("http://jsonplaceholder.typicode.com")
            response = albums.replace(1, 20, 'Reaplacement Title')
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200
    
    def test_modify_album(self):
        try:
            albums = Album("http://jsonplaceholder.typicode.com")
            response = albums.modify(4, title = 'A Modified Title')
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200
    
    def test_delete_valid_album(self):
        try:
            albums = Album("http://jsonplaceholder.typicode.com")
            response = albums.delete(2)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_delete_invalid_album(self):
        try:
            albums = Album("http://jsonplaceholder.typicode.com")
            response = albums.delete(5000)
        except err.HTTPError:
            assert True
