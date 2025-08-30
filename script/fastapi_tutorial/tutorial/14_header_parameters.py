"""
cookie와 마찬가지로 아직은 감이 잘 안옴...
"""

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items")
async def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("14_header_parameters:app", reload=True, port=8456)
