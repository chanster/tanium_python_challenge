from requests import exceptions as err
from ..post import Post
import pytest


class TestPost():

    def test_get_all_posts(self):
        try:
            posts = Post("http://jsonplaceholder.typicode.com")
            response = posts.get()
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_get_single_post(self):
        try:
            posts = Post("http://jsonplaceholder.typicode.com")
            response = posts.get(5)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_add_post(self):
        try:
            posts = Post("http://jsonplaceholder.typicode.com")
            response = posts.add(1, 'This is a Test', 'A test to add an item to the posts resource')
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 201
    
    def test_replace_post(self):
        try:
            posts = Post("http://jsonplaceholder.typicode.com")
            response = posts.replace(1,2, 'Replacement Ttile', 'Replacement body message.')
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_modify_post(self):
        try:
            posts =  Post("http://jsonplaceholder.typicode.com")
            response = posts.modify(1, user_id = 7)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_delete_valid_post(self):
        try:
            posts =  Post("http://jsonplaceholder.typicode.com")
            response = posts.delete(1)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_delete_invalid_post(self):
        try:
            posts = Post("http://jsonplaceholder.typicode.com")
            response = posts.delete(1000)
        except err.HTTPError:
            assert True
