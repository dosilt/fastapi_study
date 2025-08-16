"""
FastAPI의 가장 기본적인 사용법
requests.get({ip})를 치면 app.get('/') 부분이 실행됨

python script로 uvicorn {python file}:app --reload 하거나
uvicorn.run({python file}:app, reload=True) 로 실행

--reload의 기능은 백엔드 코드가 수정될 때, 재실행 없이 바로 적용됨
"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'hello world'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("01_first_steps:app", reload=True, port=8000)