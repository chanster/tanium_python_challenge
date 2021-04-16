import requests

class Post:
    
    def __init__(self, entrypoint):
        self.entrypoint = f"{entrypoint}/posts"

    if __name__ == "__main__":
        print(f"Entrypoint: {entrypoint}")

    def get(self, post_id = None):
        '''GET request to posts resource'''
        # get all posts of no post id defined
        if post_id:
            response = requests.get(f"{self.entrypoint}/{post_id}")
            response.raise_for_status()
        # get specific post id
        else:
            response = requests.get(f"{self.entrypoint}")
            response.raise_for_status()
        
        return response

    def add(self, user_id, title, body):
        '''POST request to posts resource'''
        headers = {
            'Content-Type': 'application/json'
        }
        content = {
            'title': title,
            'body': body,
            'userId': user_id
        }

        response = requests.post(self.entrypoint, json = content, headers = headers)
        response.raise_for_status()

        return response

    def replace(self, post_id, user_id, title, body):
        '''PUT request to a specified posts resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {
            'title': title,
            'body': body,
            'userId': user_id
        }

        response = requests.put(f"{self.entrypoint}/{post_id}", json = content, headers = headers)
        response.raise_for_status()

        return response


    def modify(self, post_id, user_id, title = None, body = None):
        '''PATCH request to a specified posts resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {}
        if user_id : content['userId'] =  user_id
        if title :  content['title'] = title
        if body : content['body'] = body 

        response = requests.patch(f"{self.entrypoint}/{post_id}", json = content, headers = headers)
        response.raise_for_status()

        return response


    def delete(self, post_id):
        '''DELETE request to a specified post resource'''
        response = requests.delete(f"{self.entrypoint}/{post_id}")
        response.raise_for_status()

        return response

    def filter(self, filters):
        pass
