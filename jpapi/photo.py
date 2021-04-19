from urllib.parse import urlencode
import requests

class Photo:
    
    def __init__(self, entrypoint):
        self.entrypoint = f"{entrypoint}/photos"

    if __name__ == "__main__":
        print(f"Entrypoint: {entrypoint}")

    def get(self, photo_id = None):
        '''GET request to photos resource'''
        # get all photos if no photos id defined
        if photo_id:
            response = requests.get(f"{self.entrypoint}/{photo_id}")
            response.raise_for_status()
        # get specific photo id
        else:
            response = requests.get(f"{self.entrypoint}")
            response.raise_for_status()

        return response

    def add(self, album_id, title, url, thumbnail):
        '''POST request to photos resource'''
        headers = {
            'Content-Type': 'application/json'
        }
        content = {
            'albumId': album_id,
            'title': title,
            'url': url,
            'thumbnail': thumbnail
        }

        response = requests.post(self.entrypoint, json = content, headers = headers)
        response.raise_for_status()

        return response

    def replace(self, photo_id, album_id, title, url, thumbnail):
        '''PUT request to a specified photos resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {
            'albumId': album_id,
            'title': title,
            'url': url,
            'thumbnail': thumbnail
        }

        response = requests.put(f"{self.entrypoint}/{photo_id}", json = content, headers = headers)
        response.raise_for_status()

        return response


    def modify(self, photo_id, album_id = None, title = None, url = None, thumbnail = None):
        '''PATCH request to a specified photos resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {}
        if album_id : content['albumId'] =  album_id
        if title :  content['title'] = title
        if url : content['body'] = url
        if thumbnail : content['thumbnail'] = thumbnail 

        response = requests.patch(f"{self.entrypoint}/{photo_id}", json = content, headers = headers)
        response.raise_for_status()

        return response


    def delete(self, photo_id):
        '''DELETE request to a specified photos resource'''
        response = requests.delete(f"{self.entrypoint}/{photo_id}")
        response.raise_for_status()

        return response

    def filter(self, album_id = None):
        filters = {}
        if album_id : filters['albumId'] = album_id

        response = requests.get(f"{self.entrypoint}?{urlencode(filters)}")
        response.raise_for_status()

        return response
