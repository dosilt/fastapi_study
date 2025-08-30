from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post('/files')
async def create_file(file: bytes = File()):
    print(len(file))
    return {'file_size': len(file)}

@app.post('/upload_files')
async def create_upload_file(file: UploadFile):
    print(file)
    return {'filename': file.filename}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run('22_request_files:app', reload=True, port=8456)