'''modules for api client'''
from urllib.parse import urlencode
import requests


class Post:
    '''Class for JSON Placement posts resource'''
    def __init__(self, entrypoint):
        self.entrypoint = f"{entrypoint}/posts"

    def get(self, post_id = None):
        '''get specific post or all posts'''
        # get specific post id
        if post_id:
            response = requests.get(f"{self.entrypoint}/{post_id}")
            response.raise_for_status()
        # get all posts of no post id defined
        else:
            response = requests.get(f"{self.entrypoint}")
            response.raise_for_status()

        return response

    def get_comments(self, post_id):
        '''get comments of a speicifc post'''
        response = requests.get(f"{self.entrypoint}/{post_id}/comments")
        response.raise_for_status()

        return response

    def add(self, user_id, title, body):
        '''add a new post'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {
            'title': title,
            'body': body,
            'userId': user_id
        }

        response = requests.post(
            self.entrypoint,
            json = content,
            headers = headers
        )

        response.raise_for_status()

        return response

    def replace(self, post_id, user_id, title, body):
        '''completely replace a post'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {
            'title': title,
            'body': body,
            'userId': user_id
        }

        response = requests.put(
            f"{self.entrypoint}/{post_id}",
            json = content,
            headers = headers
        )

        response.raise_for_status()

        return response

    def modify(self, post_id, user_id = None, title = None, body = None):
        '''modify parts of a post'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }

        content = {}
        if user_id : content['userId'] =  user_id
        if title :  content['title'] = title
        if body : content['body'] = body

        response = requests.patch(
            f"{self.entrypoint}/{post_id}",
            json = content,
            headers = headers
        )

        response.raise_for_status()

        return response

    def delete(self, post_id):
        '''delete a specific post'''
        response = requests.delete(f"{self.entrypoint}/{post_id}")
        response.raise_for_status()

        return response

    def filter(self, user_id = None):
        '''filter posts'''
        filters = {}
        if user_id: filters['userId'] = user_id

        response = requests.get(f"{self.entrypoint}?{urlencode(filters)}")
        response.raise_for_status()

        return response
