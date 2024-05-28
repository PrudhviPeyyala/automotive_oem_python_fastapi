import requests


def users():
    response = requests.get('http://localhost:7000/users')
    return response.json()
