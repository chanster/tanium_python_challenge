from urllib.parse import urlencode
import requests

class Todo:
    
    def __init__(self, entrypoint):
        self.entrypoint = f"{entrypoint}/todos"

    if __name__ == "__main__":
        print(f"Entrypoint: {entrypoint}")

    def get(self, todo_id  = None):
        '''GET request to todos resource'''
        # get all todos of no post id defined
        if todo_id :
            return requests.get(f"{self.entrypoint}/{todo_id}")
        # get specific post id
        else:
            return requests.get(f"{self.entrypoint}")

    def add(self, title, completed = False):
        '''POST request to todos resource'''
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

    def replace(self, todo_id, title, completed):
        '''PUT request to a specified todos resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {
            'title': title,
            'completed': completed
        }

        response = requests.put(f"{self.entrypoint}/{todo_id}", json = content, headers = headers)
        response.raise_for_status()

        return response

    def modify(self, todo_id, title = None, completed = None):
        '''PATCH request to a specified todos resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {}
        if title :  content['title'] = title
        # modify if either True or False
        if completed != None : content['body'] = completed

        response = requests.patch(f"{self.entrypoint}/{todo_id}", json = content, headers = headers)
        response.raise_for_status()

        return response

    def delete(self, todo_id ):
        '''DELETE request to a specified post resource'''
        return requests.delete(f"{self.entrypoint}/{todo_id}")

    def filter(self, user_id = None, completed = None):
        filters = {}
        if user_id : filters['userId'] = user_id
        # convert Boolean to lowercase string to match query
        if completed != None : filters['completed'] = ''.format(completed).lower()
        
        response = requests.delete(f"{self.entrypoint}?{urlencode(filters)}")
        response.raise_for_status()

        return response
