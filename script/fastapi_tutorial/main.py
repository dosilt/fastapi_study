import requests

url = f'http://localhost:8000/items/hello'

data = {'q': 1, 'short': False}

response = requests.get(url, params=data)
print(response.json())