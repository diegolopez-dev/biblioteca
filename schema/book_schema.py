from pydantic import BaseModel

class BookSchema(BaseModel):
    id: int | None = None
    name: str
    autor: str
    rating: float