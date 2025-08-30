from typing import Any, List, Union, Annotated

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: Union[float, None] = None
#     tags: List[str] = []


# @app.post("/items", response_model=Item)
# async def create_item(item: Item) -> Any:
#     return item


# @app.get("/items", response_model=List[Item])
# async def read_items() -> Any:
#     return [
#         {"name": "Portal Gun", "price": 42.0},
#         {"name": "Plumbus", "price": 32.0},
#     ]

# -----------------------------------------------------------

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None


# # @app.post("/user", response_model=UserOut)
# @app.post("/user")
# async def create_user(user: UserIn) -> UserOut:
#     return user


# -----------------------------------------------------------


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model_exclude_unset=True)
async def read_item(item_id: str) -> Item:
    return items[item_id]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("17_response_model_return_type:app", reload=True, port=8456)
