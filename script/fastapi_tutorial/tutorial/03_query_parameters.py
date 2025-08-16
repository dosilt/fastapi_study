"""
변수를 인자로 받을 수 있는 api 함수 선언 방식
변수 뒤에 자료형 지정 가능
변수 뒤에 default 값 지정 가능
변수의 입력이 없을 경우에는 에러 발생 (None 값이라도 나오도록 셋팅해놔야됨.)
"""

from fastapi import FastAPI

app = FastAPI()

fake_tiems_db = [{'item_name': 'Foo'}, {'item_name': 'Bar'}, {'item_name': 'Baz'}]

# @app.get('/items/')
# async def read_item(skip: int=0, limit: int=10):
#     return fake_tiems_db[skip:skip+limit]

# ------------------------------------------

# @app.get('/items/{item_id}')
# async def read_item(item_id: str, q: str|None=None):
#     if q:
#         return {'item_id': item_id, 'q':q}
#     return {'item_id': item_id}

# ------------------------------------------

@app.get('/items/{item_id}')
async def read_item(item_id: str, q: str|None=None, short:bool=False):
    item = {'item_id': item_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update(
            {'description': 'This is an amazing item that has a long description'}
        )
    return item

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('03_query_parameters:app', reload=True, port=8000)