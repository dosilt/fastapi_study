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

# 12번 - Extra Data Types 테스트
import uuid
from datetime import datetime, time, timedelta

# UUID 생성
item_uuid = str(uuid.uuid4())
print(f"Generated UUID: {item_uuid}")

url = f"http://localhost:8456/items/{item_uuid}"
response = requests.put(
    url,
    json={
        "start_datetime": "2024-01-15T10:30:00",  # ISO 형식
        "end_datetime": "2024-01-15T18:30:00",    # ISO 형식  
        "process_after": 3600,                    # 1시간 (초 단위)
        "repeat_at": "14:30:00"                   # 매일 반복 시간
    }
)

print("Response:")
print(response.json())
