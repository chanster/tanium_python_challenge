import requests

class Album:
    
    def __init__(self, entrypoint):
        self.entrypoint = f"{entrypoint}/albums"

    if __name__ == "__main__":
        print(f"entrypoint: {entrypoint}/albums")

    def get(self, album_id = None):
        '''GET request to posts resource'''
        # get all posts of no post id defined
        if album_id:
            response = requests.get(f"{self.entrypoint}/{album_id}")
        # get specific post id
        else:
            response = requests.get(f"{self.entrypoint}")
        
        response.raise_for_status()

        return response

    def get_photos(self, album_id):
        response = requests.get(f"{self.entrypoint}/{album_id}/photos")
        response.raise_for_status()

        return response

    def add(self, user_id, title):
        '''POST request to posts resource'''
        headers = {
            'Content-Type': 'application/json'
        }
        content = {
            'title': title,
            'userId': user_id
        }

        response = requests.post(self.entrypoint, json = content, headers = headers)
        response.raise_for_status()

        return response

    def replace(self, album_id, user_id, title):
        '''PUT request to a specified posts resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {
            'title': title,
            'userId': user_id
        }

        response = requests.put(f"{self.entrypoint}/{album_id}", json = content, headers = headers)
        response.raise_for_status()

        return response

    def modify(self, album_id, user_id = None, title = None):
        '''PATCH request to a specified posts resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {}
        if user_id : content['userId'] =  user_id
        if title :  content['title'] = title

        response = requests.patch(f"{self.entrypoint}/{album_id}", json = content, headers = headers)
        response.raise_for_status()

        return response


    def delete(self, album_id):
        '''DELETE request to a specified post resource'''
        response = requests.delete(f"{self.entrypoint}/{album_id}")
        response.raise_for_status()

        return response
