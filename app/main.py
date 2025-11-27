from fastapi import FastAPI
from app.routes_books import router as books_router
from fastapi.responses import RedirectResponse

app = FastAPI(title="Books API with Supabase & Gemini")

app.include_router(books_router)

@app.get("/")
def root():
   return RedirectResponse("/docs")
