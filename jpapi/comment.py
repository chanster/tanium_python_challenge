'''modules for api client'''
from urllib.parse import urlencode
import requests


class Comment:
    '''Class for JSON Placement comments resource'''
    def __init__(self, entrypoint):
        self.entrypoint = f"{entrypoint}/comments"

    def get(self, comment_id = None):
        '''get all or single comment'''
        # get all posts of no post id defined
        if comment_id:
            response = requests.get(f"{self.entrypoint}/{comment_id}")
        # get specific post id
        else:
            response = requests.get(f"{self.entrypoint}")

        response.raise_for_status()

        return response

    def add(self, post_id, name, email, body):
        '''add a comment to post'''
        headers = {
            'Content-Type': 'application/json'
        }
        content = {
            'PostId': post_id,
            'name': name,
            'email': email,
            'body': body
        }

        response = requests.post(self.entrypoint, json = content, headers = headers)
        response.raise_for_status()

        return response

    def replace(self, comment_id, post_id, name, email, body):
        '''repalce a comment'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {
            'PostId': post_id,
            'name': name,
            'email': email,
            'body': body
        }

        response = requests.put(f"{self.entrypoint}/{comment_id}", json = content, headers = headers)
        response.raise_for_status()

        return response

    def modify(self, comment_id, post_id = None, name = None, email = None, body = None):
        '''modify a comment'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {}
        if post_id : content['postId'] =  post_id
        if name :  content['name'] = name
        if email : content['email'] = email
        if body : content['body'] = body

        response = requests.patch(f"{self.entrypoint}/{comment_id}", json = content, headers = headers)
        response.raise_for_status()

        return response

    def delete(self, comment_id):
        '''delete a specific comment'''
        response = requests.delete(f"{self.entrypoint}/{comment_id}")
        response.raise_for_status()

        return response

    def filter(self, user_id = None, post_id = None, email = None):
        '''filter comments'''
        filters = {}
        if post_id : filters['postId'] = post_id
        if user_id : filters['userId'] = user_id
        if email : filters['email'] = email
        
        response = requests.get(f"{self.entrypoint}", params = urlencode(filters))
        response.raise_for_status()

        return response
