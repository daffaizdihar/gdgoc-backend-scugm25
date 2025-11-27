from fastapi import APIRouter, HTTPException
from app.schemas import BookCreate, BookUpdate
from app.crud import *
from app.gemini import generate_summary_and_genre

router = APIRouter(prefix="/rest/v1/books", tags=["Books"])

# CREATE
@router.post("")
async def create_book(book: BookCreate):
   # Generate summary + genre from Gemini
   ai = await generate_summary_and_genre(book.title, book.author, book.year)

   payload = {
      "title": book.title,
      "author": book.author,
      "year": book.year,
      "summary": ai.get("summary", ""),
      "genre": ai.get("genre", "")
   }

   created = create_book_in_db(payload)

   return {
      "message": "Book created",
      "data": created
   }


# LIST
@router.get("")
def list_books():
   books = get_all_books()
   return {"data": books}


# GET DETAIL
@router.get("/{book_id}")
def get_book_detail(book_id: int):
   book = get_book_by_id(book_id)
   if not book:
      raise HTTPException(status_code=404, detail="Book not found")
   return {"data": book}


# UPDATE
@router.put("/{book_id}")
def update_book_data(book_id: int, update_data: BookUpdate):
   book = update_book(book_id, update_data.dict(exclude_unset=True))
   if not book:
      raise HTTPException(status_code=404, detail="Book not found")
   return {
      "message": "Book updated",
      "data": book
   }


# DELETE
@router.delete("/{book_id}")
def delete_book_data(book_id: int):
   deleted = delete_book(book_id)
   return {"message": f"Book {book_id} deleted"}
