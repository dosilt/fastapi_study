import requests

# url = f'http://localhost:8000/items'
# data = {'name': 'hello', 'description': 'test', 'price': 5000, 'tax': 500}
# response = requests.post(url, json=data)

# url = f'http://localhost:8000/items/13'
# response = requests.put(url, json=data)


# url = 'http://localhost:8000/items/'
# response = requests.get(url, params={"item-query": 'fixedquery'})
# response = requests.get(url)


# url = "http://localhost:8456/items/1"
# response = requests.put(
#     url,
#     # params={"q": 1},
#     json={
#         "item": {"name": "laptop", "price": 1000.0, "tax": 100.0},
#         # "user": {"username": "hello", "full_name": "mister"},
#         # "importance": 5,
#     },
# )

url = "http://localhost:8456/items/1"
response = requests.put(
    url,
    json={
        "item": {
            "name": "laptop",
            "price": 500,
            "image": [{"url": "http://example.com/baz.jpg", "name": "The Foo live"}],
        }
    },
)

print(response.json())
