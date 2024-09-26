from fastapi import FastAPI
import uvicorn
from sockets import sio_app

app = FastAPI()
app.mount('/', app=sio_app)

@app.get('/')
async def home():
    return {"message" : "Hello"}

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)