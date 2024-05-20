from fastapi import APIRouter, Response, status, Request, Form 
from schema.book_schema import BookSchema
from fastapi.responses import HTMLResponse
from model.books import books
from config.db import engine
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

templates = Jinja2Templates(directory="./public/templates")

router = APIRouter()

@router.get("/", response_model=List[BookSchema], response_class=HTMLResponse)
def get_books(request: Request):
    with engine.connect() as conn:
        all_books = conn.execute(books.select()).fetchall()
        conn.commit()
        return templates.TemplateResponse(request=request, name="index.html", context={"all_books": all_books})
    
@router.get("/add")
async def add(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})

@router.get("/other")
async def other(request: Request):
    return templates.TemplateResponse("other.html", {"request": request})

@router.get("/edit/{book_id}", response_model=List[BookSchema], response_class=HTMLResponse)
async def edit(request: Request, book_id: int):
    with engine.connect() as conn:
        book = conn.execute(books.select().where(books.c.id == book_id)).first()
        return templates.TemplateResponse(request=request, name="update.html", context={"book": book})

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_book(name: str = Form(...), autor: str = Form(...), rating: float = Form(...)):
    with engine.connect() as conn:
        check_book = conn.execute(books.select().where(books.c.name == name)).first()
        check_rating = conn.execute(books.select().where(books.c.rating== rating)).first()
        if check_book != None:
            return RedirectResponse(url=router.url_path_for("other"), status_code=status.HTTP_303_SEE_OTHER)
        else:
            conn.execute(books.insert().values(
                name = name, 
                autor = autor, 
                rating = rating
            ))
            conn.commit()
        return RedirectResponse(url=router.url_path_for("get_books"), status_code=status.HTTP_303_SEE_OTHER)

@router.post("/update/{book_id}")
async def update(book_id: int, name: str = Form(...), autor: str = Form(...), rating: float = Form(...)):
    with engine.connect() as conn:
        conn.execute(books.update().values(
            name = name, 
            autor = autor, 
            rating = rating).where(books.c.id == book_id))
        conn.commit()
        return RedirectResponse(url=router.url_path_for("get_books"), status_code=status.HTTP_303_SEE_OTHER)

@router.get("/delete/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(book_id: str):
    with engine.connect() as conn:
        conn.execute(books.delete().where(books.c.id == book_id))
        conn.commit()
        return RedirectResponse(url=router.url_path_for("get_books"), status_code=status.HTTP_303_SEE_OTHER)