from app.database import supabase

def create_book_in_db(data):
   response = supabase.table("books").insert(data).execute()
   return response.data[0]

def get_all_books():
   return supabase.table("books").select("*").order("id", desc=False).execute().data

def get_book_by_id(book_id: int):
   resp = supabase.table("books").select("*").eq("id", book_id).execute()
   return resp.data[0] if resp.data else None

def update_book(book_id: int, data):
   resp = supabase.table("books").update(data).eq("id", book_id).execute()
   return resp.data[0] if resp.data else None

def delete_book(book_id: int):
   return supabase.table("books").delete().eq("id", book_id).execute()
