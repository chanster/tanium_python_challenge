import requests


class ApiClient:

    def __init__(self, endpoint = 'https://jsonplaceholder.typicode.com'):
        self.endpoint = endpoint

    class Posts:

        def get(self, post_id = ''):
            '''GET request to posts resource'''
            # get all posts of no post id defined
            if post_id != '':
                return requests.get(f"{self.endpoint}/posts/{str(post_id)}")
            # get specific post id
            else:
                return requests.get(f"{self.endpoint}/posts")

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

            return request.post(self.endpoint, json = content, header = headers)

        def replace(self, post_id, title, body, user_id)
            '''PUT request to a specified posts resource'''
            headers = {
                'Content-Type': 'application/json; charset=UTF-8'
            }
            content = {
                'id': post_id,
                'title': title,
                'body': body
                'userId': user_id
            }

            return request.put(self.endpoint, json = content, header = headers)


        def modify(self, post_id, title = '', body = '', user_id)
            '''PATCH request to a specified posts resource'''
            headers = {
                'Content-Type': 'application/json; charset=UTF-8'
            }
            content = {
                'id': post_id,
                'userId': user_id
            }
            if title != '' :  content['title'] = title
            if body != '' : content['body'] = body 

            return request.patch(f"{self.endpoint}/posts", json = content, header = headers)


        def delete(self, post_id):
            '''DELETE request to a specified post resource'''
            return request.delete(f"{self.endpoint}/posts/{str(post_id)}")

        def search(self, filter)


    class Comments:

    class Albums:

    class Todos:

    class Users:

