import requests

item_id = 'alexnet'
url = f'http://localhost:8000/models/{item_id}'

response = requests.get(url)
print(response.json())