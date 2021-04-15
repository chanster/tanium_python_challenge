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

        return requests.post(self.entrypoint, json = content, headers = headers)

    def replace(self, todo_id, title, completed):
        '''PUT request to a specified todos resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {
            'title': title,
            'completed': completed
        }

        return requests.put(f"{self.entrypoint}/{todo_id}", json = content, headers = headers)


    def modify(self, todo_id, title = None, completed = None):
        '''PATCH request to a specified todos resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {}
        if title :  content['title'] = title
        # modify if either True or False
        if completed != None : content['body'] = completed

        return requests.patch(f"{self.entrypoint}/{todo_id}", json = content, headers = headers)


    def delete(self, todo_id ):
        '''DELETE request to a specified post resource'''
        return requests.delete(f"{self.entrypoint}/{todo_id}")

    def filter(self, filters):
        pass
