from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from database import get_connection
from typing import Optional

class Book(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    author: str = Field(..., min_length=3, max_length=100)
    publisher: str = Field(..., min_length=3, max_length=100)
    image_url: str

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    image_url: Optional[str] = None


app = FastAPI()


@app.post("/create")
def add_book(book: Book):

    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO books (title, author, publisher, image_url)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """, (book.title, book.author, book.publisher, book.image_url))

    new_id = cur.fetchone()[0]

    con.commit()
    con.close()

    return {"message": "New book added successfully.","id": new_id}


@app.get("/search/book")
def search_books(q: str = Query(..., min_length=3, max_length=100),page: int = 1,size: int = 3):

    con = get_connection()
    cur = con.cursor()

    offset = (page - 1) * size

    cur.execute("""
        SELECT id, title, author, publisher, image_url
        FROM books
        WHERE title ILIKE %s
           OR author ILIKE %s
           OR publisher ILIKE %s
        OFFSET %s LIMIT %s;
    """, (f"%{q}%", f"%{q}%", f"%{q}%", offset, size))

    results = cur.fetchall()

    cur.execute("""
        SELECT COUNT(*)
        FROM books
        WHERE title ILIKE %s
           OR author ILIKE %s
           OR publisher ILIKE %s;
    """, (f"%{q}%", f"%{q}%", f"%{q}%"))

    total = cur.fetchone()[0]

    con.close()

    return {"message": "Search completed successfully.","Total Results": total,"page": page,"size": size,"Results": results}


#NEW ENDPOINTS START FROM HERE 
@app.get("/search/author") # -> THE ACTUAL NEW TASK: SEARCHES FOR AUTHORS AND THEIR BOOKS COUNT
def search_author(q: str = Query(..., min_length=3, max_length=100), page: int = 1, size: int = 3):
    con = get_connection()
    cur = con.cursor()

    offset = (page - 1) * size

    cur.execute("""
        SELECT author, COUNT(*) AS books_count
        FROM books
        WHERE author ILIKE %s
        GROUP BY author
        ORDER BY books_count
""", (f"%{q}%",))
    
    result = cur.fetchall()
    con.close()

    final_result = [{"author":r[0], "books_count":r[1]} for r in result]

    return {"message":"Search completed succesfully.", "query":q, "result":final_result}


@app.patch("/update/book/{book_id}")
def update_book(book_id: int, book: BookUpdate):

    con = get_connection()
    cur = con.cursor()

    fields = []
    updating_materials = []

    if book.title is not None:
        fields.append("title = %s")
        updating_materials.append(book.title)

    if book.author is not None:
        fields.append("author = %s")
        updating_materials.append(book.author)

    if book.publisher is not None:
        fields.append("publisher = %s")
        updating_materials.append(book.publisher)

    if book.image_url is not None:
        fields.append("image_url = %s")
        updating_materials.append(book.image_url)

    if not fields:
        return {"error": "You haven't chose any field to update."}

    updating_materials.append(book_id)

    q = f"""
        UPDATE books
        SET {", ".join(fields)}
        WHERE id = %s
        RETURNING id;
    """

    cur.execute(q, updating_materials)
    updated_book = cur.fetchone()

    con.commit()
    con.close()

    if update_book is None:
        return {"error": "Book not found."}

    return {"message": "Book updated successfully.", "id": book_id}


@app.delete("/delete/book/{book_id}")
def delete_book(book_id: int):

    con = get_connection()
    cur = con.cursor()

    cur.execute("""
            DELETE FROM books 
            WHERE id = %s 
            RETURNING id;
            """, (book_id,))
    
    deleted_book = cur.fetchone()

    con.commit()
    con.close()

    if deleted_book is None:
        return {"error": "Book not found."}

    return {"message": "Book deleted successfully.", "id": book_id}
