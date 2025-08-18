from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_itmes(
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: str | None = Query(default=None, alias="item-query"),
    size: float = Query(gt=0, lt=10.5),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("06_path_parameters_and_numeric_validations:app", reload=True, port=8456)
