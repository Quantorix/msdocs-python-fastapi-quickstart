from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run('myapp:app', host='0.0.0.0', port=8000)

