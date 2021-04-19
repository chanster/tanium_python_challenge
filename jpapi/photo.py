'''modules for api client'''
from urllib.parse import urlencode
import requests


class Photo:
    '''Class for JSON Placement photos resource'''
    def __init__(self, entrypoint):
        self.entrypoint = f"{entrypoint}/photos"

    def get(self, photo_id = None):
        '''get all or single photo resource'''
        if photo_id:
            # get all photos if no photos id defined
            response = requests.get(f"{self.entrypoint}/{photo_id}")
        else:
            # get specific photo id
            response = requests.get(f"{self.entrypoint}")

        response.raise_for_status()

        return response

    def add(self, album_id, title, url, thumbnail):
        '''add a photo'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
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
        '''replace a specific photo'''
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
        '''modify a specific photo'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {}
        if album_id:
            content['albumId'] =  album_id
        if title:
            content['title'] = title
        if url:
            content['body'] = url
        if thumbnail:
            content['thumbnail'] = thumbnail

        response = requests.patch(
            f"{self.entrypoint}/{photo_id}",
            json = content,
            headers = headers
        )
        response.raise_for_status()

        return response


    def delete(self, photo_id):
        '''delete a specific photo'''
        response = requests.delete(f"{self.entrypoint}/{photo_id}")
        response.raise_for_status()

        return response

    def filter(self, album_id = None):
        '''fliter on photos'''
        filters = {}
        if album_id:
            filters['albumId'] = album_id

        response = requests.get(f"{self.entrypoint}", params = urlencode(filters))
        response.raise_for_status()

        return response
