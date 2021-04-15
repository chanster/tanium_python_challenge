import requests

class Album:
    
    def __init__(self, entrypoint):
        self.entrypoint = f"{entrypoint}/albums"

    if __name__ == "__main__":
        print(f"entrypoint: {entrypoint}")

    def get(self, album_id = None):
        '''GET request to posts resource'''
        # get all posts of no post id defined
        if album_id:
            return requests.get(f"{self.entrypoint}/{album_id}")
        # get specific post id
        else:
            return requests.get(f"{self.entrypoint}")

    def add(self, user_id, title):
        '''POST request to posts resource'''
        headers = {
            'Content-Type': 'application/json'
        }
        content = {
            'title': title,
            'userId': user_id
        }

        return requests.post(self.entrypoint, json = content, header = headers)

    def replace(self, album_id, user_id, title):
        '''PUT request to a specified posts resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {
            'title': title,
            'userId': user_id
        }

        return requests.put(self.entrypoint, json = content, header = headers)


    def modify(self, album_id, user_id = None, title = None):
        '''PATCH request to a specified posts resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {}
        if user_id : content['userId'] =  user_id
        if title :  content['title'] = title

        return requests.patch(f"{self.entrypoint}/{album_id}", json = content, header = headers)


    def delete(self, album_id):
        '''DELETE request to a specified post resource'''
        return requests.delete(f"{self.entrypoint}/{album_id}")

    def search(self, filter):
        pass