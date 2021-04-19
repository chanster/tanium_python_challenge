import requests

class User:
    
    def __init__(self, entrypoint):
        self.entrypoint = f"{entrypoint}/users"

    if __name__ == "__main__":
        print(f"Entrypoint: {entrypoint}")

    def get(self, user_id = None):
        '''get specific user or all users'''
        # get all users of no post id defined
        if user_id:
            return requests.get(f"{self.entrypoint}/{user_id}")
        # get specific post id
        else:
            return requests.get(f"{self.entrypoint}")

    def add(self, name, username, email, address, phone, website, company):
        '''add a user'''
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

        response = requests.post(self.entrypoint, json = content, headers = headers)
        response.raise_for_status()

        return response

    def replace(self, user_id, name, username, email, address, phone, website, company):
        '''replace a user'''
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

        response = requests.put(f"{self.entrypoint}/{user_id}", json = content, headers = headers)
        response.raise_for_status()

        return response


    def modify(self, user_id, name= None, username = None, email = None, address = None, phone = None, website = None, company = None):
        '''modify a user'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        content = {}
        # Add to content dict if args has values
        if name : content['name'] =  name
        if username : content['username'] = username
        if email : content['email'] =  email
        if address : content['address'] = address
        if phone : content['phone'] = phone
        if website : content['website'] = website
        if company : content['company'] = company

        response = requests.patch(f"{self.entrypoint}/{user_id}", json = content, headers = headers)
        response.raise_for_status()

        return response

    def delete(self, user_id):
        '''delete a specific user'''
        response = requests.delete(f"{self.entrypoint}/{user_id}")
        response.raise_for_status()

        return response

    def filter(self, filters):
        pass
