"""
FastAPI의 path parameter사용법
데코레이터에 추가적인 정보 지시 및 함수의 첫번째 인자로 넘김
url입력할 때, 같이 입력해야됨 (함수의 인자로써 넘겨 주는 것이 아님.)
- 주의 사항으로는 "/" 으로 연결된 인자를 넘겨주면 안됨
- "/"로 된 인자를 넘겨 주고 싶으면 {file_path:path} 로 경로라는 것을 알려줘야함.

Enum을 이용해서 함수에 들어올 수 있는 입력을 제한할 수 있음
- 이외의 입력에 대해서는 에러가 출력됨
"""

from fastapi import FastAPI

app = FastAPI()

# @app.get('/items/{item_id}')
# async def read_item(item_id):
#     return {'item_id': item_id}

# ----------------------------------------

# @app.get('/items/{item_id}')
# async def read_item(item_id: int):
#     return {'item_id': item_id}

# ----------------------------------------

# @app.get('/users/me')
# async def read_user_me():
#     return {'user_id': 'the current user'}

# @app.get('/users/{user_id}')
# async def read_user(user_id: str):
#     return {'user_id': user_id}

# ----------------------------------------

from enum import Enum

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'
    
@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Learning FTW!'}
    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}

    return {'model_name': model_name, 'message': 'Have some residuals'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("02_path_parameters:app", reload=True, port=8000)