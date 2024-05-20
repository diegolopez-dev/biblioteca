from fastapi import FastAPI, Request
from router.router import router
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="./public/static"), name="static")
templates = Jinja2Templates(directory="./public/templates")
app.include_router(router)