from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
   title: str
   author: str
   year: int

class BookUpdate(BaseModel):
   title: Optional[str] = None
   author: Optional[str] = None
   year: Optional[int] = None
   summary: Optional[str] = None
   genre: Optional[str] = None

class Book(BaseModel):
   id: int
   title: str
   summary: str
   genre: str
   author: str
   year: int

   class Config:
      orm_mode = True
