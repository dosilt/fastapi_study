import requests

# url = f'http://localhost:8000/items'
# data = {'name': 'hello', 'description': 'test', 'price': 5000, 'tax': 500}
# response = requests.post(url, json=data)

# url = f'http://localhost:8000/items/13'
# response = requests.put(url, json=data)


# url = 'http://localhost:8000/items/'
# response = requests.get(url, params={"item-query": 'fixedquery'})
# response = requests.get(url)


url = "http://localhost:8456/items"
response = requests.get(url, params={"limit": 50})
print(response.json())
