from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from uploadFile import uploade_router
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))

# 템플릿 객체 초기화
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return FileResponse("static/html/index.html", media_type="text/html")

@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

@app.get("/jinja2")
async def jinja2(request: Request):
    data = {"title": "FastAPI with Jinja2", "message": "Jinja2 Message"}
    return templates.TemplateResponse("index.html", {"request": request, **data})

app.include_router(uploade_router)