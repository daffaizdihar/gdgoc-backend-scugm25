# Book Management API

Backend API built with FastAPI, Supabase, and Google Gemini for automatic book summary and genre generation.

---

## Run Program

```bash
uvicorn app.main:app --reload
```

---

## Dependencies

Install individually:

```bash
pip install fastapi
pip install uvicorn
pip install supabase
pip install python-dotenv
pip install google-genai
pip install gunicorn
```

Or install all at once:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a .env file:
```ini
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_service_role_key
GEMINI_API_KEY=your_gemini_api_key
```

---

## Project Structure
```pgsql
app/
├── main.py
├── routes_books.py
├── crud.py
├── database.py
├── gemini.py
└── schemas.py
```

---

## API Endpoints
* POST /books — create book (auto summary & genre via Gemini)
* GET /books — list all books
* GET /books/{id} — get book by ID
* PUT /books/{id} — update book
* DELETE /books/{id} — delete book

Interactive documentation available at:
```bash
/docs
```






