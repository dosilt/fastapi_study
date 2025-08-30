from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

class FormData(BaseModel):
    username: str
    password: str
    model_config = {'extra': 'forbid'}

@app.post('/login')
async def login(data: Annotated[FormData, Form()]):
    return data


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('21_form_models:app', reload=True, port=8456)