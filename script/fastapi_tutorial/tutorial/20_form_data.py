from fastapi import FastAPI, Form
from typing import Annotated

app = FastAPI()

@app.post('/login')
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {'username': username}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('20_form_data:app', reload=True, port=8456)