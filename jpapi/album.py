'''modules for api client'''
import requests


class Album:
    '''Class for JSON Placement albums resource'''
    def __init__(self, entrypoint):
        self.entrypoint = f"{entrypoint}/albums"

    def get(self, album_id = None):
        '''get all or single album'''
        if album_id:
            # get all posts of no post id defined
            response = requests.get(f"{self.entrypoint}/{album_id}")

        else:
            # get specific post id
            response = requests.get(f"{self.entrypoint}")

        response.raise_for_status()

        return response

    def get_photos(self, album_id):
        '''get photos of an albums'''
        response = requests.get(f"{self.entrypoint}/{album_id}/photos")
        response.raise_for_status()

        return response

    def add(self, user_id, title):
        '''add an album'''
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
        '''replace an album'''
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
        '''modify an album'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {}
        if user_id:
            content['userId'] =  user_id
        if title:
            content['title'] = title

        response = requests.patch(
            f"{self.entrypoint}/{album_id}",
            json = content,
            headers = headers
        )
        response.raise_for_status()

        return response


    def delete(self, album_id):
        '''delete an album'''
        response = requests.delete(f"{self.entrypoint}/{album_id}")
        response.raise_for_status()

        return response
