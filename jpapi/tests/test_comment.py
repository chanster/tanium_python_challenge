from requests import exceptions as err
from ..comment import Comment
import pytest


class TestComment():

    def test_get_all_comment(self):
        try:
            comments = Comment("http://jsonplaceholder.typicode.com")
            response = comments.get()
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200
    
    def test_get_single_comment(self):
        try:
            comments = Comment("http://jsonplaceholder.typicode.com")
            response = comments.get(20)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_get_invalid_comment(self):
        try:
            comments = Comment("http://jsonplaceholder.typicode.com")
            response = comments.get(10000)
        except err.HTTPError:
            assert True
    
    def test_add_comment(self):
        try:
            comments = Comment("http://jsonplaceholder.typicode.com")
            response = comments.add(3,'Test Suite', 'test@example.nil', 'This is a test Comment')
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 201

    def test_replace_comment(self):
        try:
            comments = Comment("http://jsonplaceholder.typicode.com")
            response = comments.replace(2, 5, 'Replacement Name', 'repalce@example.nil', 'Replacement body text')
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_modify_comment(self):
        try:
            comments = Comment("http://jsonplaceholder.typicode.com")
            response = comments.modify(2, name = 'Modified Name', body = 'Modified Body text')
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_delete_valid_comment(self):
        try:
            comments = Comment("http://jsonplaceholder.typicode.com")
            response = comments.delete(2)
        except err.HTTPError:
            assert False
        finally:
            assert response.status_code == 200

    def test_delete_invalid_comment(self):
        try:
            comments = Comment("http://jsonplaceholder.typicode.com")
            response = comments.delete(30000)
        except err.HTTPError:
            assert True
