import requests

def request_handler(url, method, data = ''):
    if method == 'get':
        response = requests.get(url)
        if response.status_code == 200:
            return response
    elif method == 'post':
        response = requests.post(url, json = data)
        if response.status_code == 200:
            return response