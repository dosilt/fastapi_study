from fastapi import FastAPI

app = FastAPI()

@app.post('/items', status_code=201)
async def create_item(name: str):
    return {'name': name}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('19_response_status_code:app', reload=True, port=8456)