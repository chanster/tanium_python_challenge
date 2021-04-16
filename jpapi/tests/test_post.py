from requests import exceptions as err
from ..post import Post
import pytest


class TestPost():

    def test_get_all_posts(self):
        posts = Post("http://jsonplaceholder.typicode.com")
        response = posts.get()
        assert response.status_code == 200

    def test_get_single_post(self):
        posts = Post("http://jsonplaceholder.typicode.com")
        response = posts.get(5)
        assert response.status_code == 200
    
    def test_get_invalid_post(self):
        try:
            posts = Post("http://jsonplaceholder.typicode.com")
            response = posts.get(500)
        except err.HTTPError:
            assert True

    def test_add_valid_post(self):
        posts = Post("http://jsonplaceholder.typicode.com")
        response = posts.add(1, 'This is a Test', 'A test to add an item to the posts resource')
        assert response.status_code == 201
    
    def test_add_invalid_post(self):
        try:
            posts = Post("http://jsonplaceholder.typicode.com")
            # add post with user that doesn't exist
            response = posts.add(3000, 'Test should fail', 'body')
        except err.HTTPError:
            assert True
    
    def test_replace_post(self):
        posts = Post("http://jsonplaceholder.typicode.com")
        response = posts.replace(1,2, 'Replacement Ttile', 'Replacement body message.')
        assert response.status_code == 200

    def test_modify_post(self):
        posts =  Post("http://jsonplaceholder.typicode.com")
        response = posts.modify(1, user_id = 7)
        assert response.status_code == 200

    def test_delete_valid_post(self):
        posts =  Post("http://jsonplaceholder.typicode.com")
        response = posts.delete(1)
        assert response.status_code == 200

    def test_delete_invalid_post(self):
        try:
            posts = Post("http://jsonplaceholder.typicode.com")
            response = posts.delete(1000)
        except err.HTTPError:
            assert True
