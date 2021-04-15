import requests

class Comment:
    
    def __init__(self, entrypoint):
        self.entrypoint = f"{entrypoint}/comments"

    if __name__ == "__main__":
        print(f"Entrypoint: {entrypoint}")

    def get(self, comment_id = None):
        '''GET request to posts resource'''
        # get all posts of no post id defined
        if comment_id:
            return requests.get(f"{self.entrypoint}/{comment_id}")
        # get specific post id
        else:
            return requests.get(f"{self.entrypoint}")

    def add(self, post_id, name, email, body):
        '''POST request to posts resource'''
        headers = {
            'Content-Type': 'application/json'
        }
        content = {
            'PostId': post_id,
            'name': name,
            'email': email,
            'body': body
        }

        return requests.post(self.entrypoint, json = content, header = headers)

    def replace(self, comment_id, post_id, name, email, body):
        '''PUT request to a specified posts resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {
            'PostId': post_id,
            'name': name,
            'email': email,
            'body': body
        }

        return requests.put(self.entrypoint, json = content, header = headers)

    def modify(self, comment_id, post_id = None, name = None, email = None, body = None):
        '''PATCH request to a specified posts resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {}
        if post_id : content['postId'] =  post_id
        if name :  content['name'] = name
        if email : content['email'] = email
        if body : content['body'] = body 

        return requests.patch(f"{self.entrypoint}/{comment_id}", json = content, header = headers)

    def delete(self, comment_id):
        '''DELETE request to a specified post resource'''
        return requests.delete(f"{self.entrypoint}/{comment_id}")

    def search(self, filter):
        pass
