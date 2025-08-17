import requests

# url = f'http://localhost:8000/items'
data = {'name': 'hello', 'description': 'test', 'price': 5000, 'tax': 500}
# response = requests.post(url, json=data)

url = f'http://localhost:8000/items/13'
response = requests.put(url, json=data)
print(response.json())