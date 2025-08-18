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
# import uuid
# from datetime import datetime, time, timedelta

# # UUID 생성
# item_uuid = str(uuid.uuid4())
# print(f"Generated UUID: {item_uuid}")

# url = f"http://localhost:8456/items/{item_uuid}"
# response = requests.put(
#     url,
#     json={
#         "start_datetime": "2024-01-15T10:30:00",  # ISO 형식
#         "end_datetime": "2024-01-15T18:30:00",    # ISO 형식
#         "process_after": 3600,                    # 1시간 (초 단위)
#         "repeat_at": "14:30:00"                   # 매일 반복 시간
#     }
# )

# print("Response:")
# print(response.json())

# 13번 - Cookie 간단 테스트

# # Cookie 없이 요청
# response1 = requests.get("http://localhost:8456/items")
# print("Cookie 없음:", response1.json())

# # Cookie 있는 요청
# response2 = requests.get("http://localhost:8456/items", cookies={"ads_id": "test123"})
# print("Cookie 있음:", response2.json())

# headers = {"User-Agent": "MyCustomApp/1.0"}
# headers = {"user-agent": "MyCustomApp/1.0"}
# response = requests.get("http://localhost:8456/items", headers=headers)
# print(response.json())


# cookies = {"session_id": "user123session", "fatebook_tracker": "fb_campaign_456", "googall_tracker": "google_ads_789"}

# response = requests.get("http://localhost:8456/items", cookies=cookies)
# print("Cookie Models")
# print(response.json())


user_info = {"username": "hello", "password": "bye", "email": "asdf@naver.com"}
response = requests.post("http://localhost:8456/user", json=user_info)
print(response.json())


# response = requests.get("http://localhost:8456/items/baz")
# print(response.json())
