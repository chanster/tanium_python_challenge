'''modules for api client'''
from urllib.parse import urlencode
import requests


class Todo:
    '''Class for JSON Placement todos resource'''
    def __init__(self, entrypoint):
        self.entrypoint = f"{entrypoint}/todos"

    def get(self, todo_id  = None):
        '''get all or specific todo'''
        # get all todos of no post id defined
        if todo_id :
            response = requests.get(f"{self.entrypoint}/{todo_id}")
        # get specific post id
        else:
            response = requests.get(f"{self.entrypoint}")

        response.raise_for_status()

        return response

    def add(self, title, completed = False):
        '''add a todo'''
        headers = {
            'Content-Type': 'application/json'
        }
        content = {
            'title': title,
            'completed': completed
        }

        response = requests.post(self.entrypoint, json = content, headers = headers)
        response.raise_for_status()

        return response

    def replace(self, todo_id, user_id, title, completed):
        '''replace a todo'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {
            'userId': user_id,
            'title': title,
            'completed': completed
        }

        response = requests.put(f"{self.entrypoint}/{todo_id}", json = content, headers = headers)
        response.raise_for_status()

        return response

    def modify(self, todo_id, user_id = None, title = None, completed = None):
        '''modify a todo'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {}
        if user_id:  content['userId'] = user_id
        if title:  content['title'] = title
        # modify if either True or False
        if completed is not None: content['body'] = completed

        response = requests.patch(f"{self.entrypoint}/{todo_id}", json = content, headers = headers)
        response.raise_for_status()

        return response

    def delete(self, todo_id ):
        '''delete a todo'''
        response = requests.delete(f"{self.entrypoint}/{todo_id}")
        response.raise_for_status()

        return response

    def filter(self, user_id = None, completed = None):
        '''filter todos'''
        filters = {}
        if user_id : filters['userId'] = user_id
        # convert Boolean to lowercase string to match query
        if completed != None : filters['completed'] = ''.format(completed).lower()

        response = requests.get(f"{self.entrypoint}", params = urlencode(filters))
        response.raise_for_status()

        return response
