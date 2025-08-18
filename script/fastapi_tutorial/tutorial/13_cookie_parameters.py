from typing import Annotated

from fastapi import FastAPI, Cookie

app = FastAPI()


@app.get("/items")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("13_cookie_parameters:app", reload=True, port=8456)
