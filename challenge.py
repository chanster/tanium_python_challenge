#!/usr/bin/env python3

from jpapi import Client
from datetime import datetime
import json


challenge = Client()

# 1 Print the value of the title for post 99
try: 
    response = challenge.posts.get(99)
    json_response = response.json()
    print(json_response['title'])
except Exception as err:
    print(f"Error occurred: {err}")

# 2 Inject a field called 'time' into the results for post number 100 and print while JSON record
try:
    response = challenge.posts.get(100)
    json_response = response.json()
    json_response['time'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(json_response)
except Exception as err:
    print(f"Error occurred: {err}")

# 3 Create new posts entry with the follow values
try:
    response = challenge.posts.add(
        title = 'Security Interview Post',
        user_id = 500,
        body = "This is an insertion test with a known API"
    )
    response.raise_for_status
except Exception as err:
    print(f"Error occurred: {err}")

# 4 Determine if your post was successful, and if it was, create a tuple
if response.status_code == 201:
    json_response = response.json()
    data = (json_response['id'], response.status_code, response.headers['X-Powered-By'])
else:
    print(f"Challenge #3 failed with error {response.status_code}: {response.text}")

# 5 print tuple from step 4
print(data)

# 6 delete record from step 3
try:
    response = challenge.posts.delete(data[0])
    print(f"Status: {response.status_code}\nX-Content-Type-Options: {response.headers['X-Content-Type-Options']}")
except Exception as err:
    print(f"Error occurred: {err}")
