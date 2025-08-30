"""
- typing
    Annotated[타입, 메타데이터] -> 형태로 선언 가능
    Literal[변수1, 변수2 ...] -> 리스트처럼 이용? 입력값 제한 가능 (chap2, Enum 같은거)

- Field 각각의 변수에 대해서 제약 조건을 걸 수 있음
"""

from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("07_query_parameter_models:app", reload=True, port=8456)
