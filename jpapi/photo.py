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
            return requests.get(f"{self.entrypoint}/{photo_id}")
        # get specific photo id
        else:
            return requests.get(f"{self.entrypoint}")

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

        return requests.post(self.entrypoint, json = content, headers = headers)

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

        return requests.put(f"{self.entrypoint}/{photo_id}", json = content, headers = headers)


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

        return requests.patch(f"{self.entrypoint}/{photo_id}", json = content, headers = headers)


    def delete(self, photo_id):
        '''DELETE request to a specified photos resource'''
        return requests.delete(f"{self.entrypoint}/{photo_id}")

    def filter(self, filters):
        pass
