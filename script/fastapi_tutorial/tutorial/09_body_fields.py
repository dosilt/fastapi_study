from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, title="The description of the item", max_length=300)
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

"""
requests.put('http://localhost:8456/itmes/item_id',
    json={item: {name: '', description: '', price: '', tax: ''}})

"""


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("09_body_fields:app", reload=True, port=8456)
