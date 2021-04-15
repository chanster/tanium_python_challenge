import requests

class Post:
    
    def __init__(self, entrypoint):
        self.entrypoint = f"{entrypoint}/users"

    if __name__ == "__main__":
        print(f"Entrypoint: {entrypoint}")

    def get(self, user_id = None):
        '''GET request to users resource'''
        # get all users of no post id defined
        if user_id:
            return requests.get(f"{self.entrypoint}/{user_id}")
        # get specific post id
        else:
            return requests.get(f"{self.entrypoint}")

    def add(self, name, username, email, address, phone, website, company):
        '''POST request to users resource'''
        headers = {
            'Content-Type': 'application/json'
        }
        content = {
            'name': name,
            'username': username,
            'email': email,
            'address': address,
            'phone': phone,
            'website': website,
            'company': company
        }

        return requests.post(self.entrypoint, json = content, headers = headers)

    def replace(self, user_id, name, username, email, address, phone, website, company):
        '''PUT request to a specified users resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {
            'name': name,
            'username': username,
            'email': email,
            'address': address,
            'phone': phone,
            'website': website,
            'company': company
        }

        return requests.put(f"{self.entrypoint}/{user_id}", json = content, headers = headers)


    def modify(self, user_id, name= None, username = None, email = None, address = None, phone = None, website = None, company = None):
        '''PATCH request to a specified users resource'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {}
        # Add to conent dict if args has values
        if name : content['name'] =  name
        if username : content['username'] = username
        if email : content['email'] =  email
        if address : content['address'] = address
        if phone : content['phone'] = phone
        if website : content['website'] = website
        if company : content['company'] = company

        return requests.patch(f"{self.entrypoint}/{user_id}", json = content, headers = headers)

    def delete(self, user_id):
        '''DELETE request to a specified post resource'''
        return requests.delete(f"{self.entrypoint}/{user_id}")

    def filter(self, filters):
        pass
