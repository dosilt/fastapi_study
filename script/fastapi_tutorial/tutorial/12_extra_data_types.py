"""
UUID : primary key를 선언할 때, 이용함. str로 표현됨
datetime.datetime : datetime과 동일
datetime.date : date만 출력
datetime.time : time만 출력
datetime.timedelta : time을 초로 출력
frozenset : 요청과 입력은 set으로 취급 되지만, 응답은 list로 반환
bytes :
Decimal :
"""

from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID

from fastapi import FastAPI, Body

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time | None, Body()] = None,
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("12_extra_data_types:app", reload=True, port=8456)
