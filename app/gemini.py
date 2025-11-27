from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

import json
import re

def parse_gemini_response(text):
   # hapus ```json ... ``` kalau ada
   cleaned = re.sub(r"```json\s*|```", "", text, flags=re.IGNORECASE).strip()
   try:
      data = json.loads(cleaned)
      # pastikan key ada
      summary = data.get("summary", "")
      genre = data.get("genre", "")
      return {"summary": summary, "genre": genre}
   except json.JSONDecodeError:
      # fallback kalau masih ga bisa
      return {"summary": text, "genre": "Unknown"}


async def generate_summary_and_genre(title: str, author: str, year: int):
   prompt = f"""
   You are a book metadata generator.
   Based on this data:
   Title: {title}
   Author: {author}
   Year: {year}

   1. Provide a short 2–3 sentence summary of the book.
   2. Provide a single-word genre classification (example: Fiction, Thriller, Sci-Fi).

   Format output as JSON with keys: summary, genre.
   """

   response = client.models.generate_content(
      model="gemini-2.5-flash", contents=prompt
   )
   return parse_gemini_response(response.text)
