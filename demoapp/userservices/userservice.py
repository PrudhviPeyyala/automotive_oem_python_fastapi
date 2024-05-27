import requests


def users():
    print('external call')
    response = requests.get('http://localhost:7000/users')
    print(response)
    print(response.json())
    return response.json()
