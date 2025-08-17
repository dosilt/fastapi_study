"""
from fastapi import Query의 사용법
Query(default, title, description, min_length, max_length, deprecated)
이러한 변수들로 localhost:8000/docs에 나타낼수 있음
"""

from typing import List
from fastapi import FastAPI, Query

app = FastAPI()

# @app.get('/items/')
# async def read_items(q: str|None=Query(default=None, min_length=3, 
#                                        max_length=50, pattern="^fixedquery$")):
#     results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
#     if q:
#         results.update({'q': q})
#     return results

# ---------------------------------------------

# @app.get('/items/')
# async def read_items(q: List[str]|None = Query(default=['foo', 'bar'])):
#     query_items = {'q': q}
#     return query_items

# ---------------------------------------------

# @app.get('/items/')
# async def read_item(q: List[str]|None = Query(
#         default=None,
#         title='Query string',
#         description='Query string for the itmes to search in the database that have a good match',
#         min_length=3
#     )):
#     results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
#     if q:
#         results.update({'q': q})
#     return results

# ---------------------------------------------

@app.get("/items/")
async def read_items(q: str|None = Query(
        default=None, alias="item-query",
        min_length=3,
        max_length=50,
        pattern="^fixedquery$",
        deprecated=True
    )):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("05_query_parameters_and_string_validations:app", reload=True)