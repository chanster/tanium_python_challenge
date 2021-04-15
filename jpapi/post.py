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
            return requests.get(f"{self.entrypoint}/{post_id}")
        # get specific post id
        else:
            return requests.get(f"{self.entrypoint}")

    def add(self, title, body, user_id):
        '''POST request to posts resource'''
        headers = {
            'Content-Type': 'application/json'
        }
        content = {
            'title': title,
            'body': body,
            'userId': user_id
        }

        return requests.post(self.entrypoint, json = content, header = headers)

    def replace(self, user_id, post_id, title, body):
        '''PUT request to a specified posts resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {
            'id': post_id,
            'title': title,
            'body': body,
            'userId': user_id
        }

        return requests.put(self.entrypoint, json = content, header = headers)


    def modify(self, post_id, user_id, title = None, body = None):
        '''PATCH request to a specified posts resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {}
        if user_id : content['userId'] =  user_id
        if title :  content['title'] = title
        if body : content['body'] = body 

        return requests.patch(f"{self.entrypoint}/{post_id}", json = content, header = headers)


    def delete(self, post_id):
        '''DELETE request to a specified post resource'''
        return requests.delete(f"{self.entrypoint}/{post_id}")

    def search(self, filter):
        pass