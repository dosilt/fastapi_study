from typing import Annotated

from fastapi import Cookie, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/items")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("15_cookie_parameter_models:app", reload=True, port=8456)
