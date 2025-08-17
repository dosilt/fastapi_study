"""
GET 요청엔 body를 담지 않음
POST
PUT
DELETE

Pydantic으로 작성시 요청 본문으로 호출 해야됨 (request에서 json={data})
쿼리 매개변수 or 변수 타입 지정으로 작성시 (request에서 params={data}) 로 호출
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str|None = None
    price: float
    tax: float|None = None
    
@app.post('/items/')
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('04_request_body:app', reload=True, port=8000)