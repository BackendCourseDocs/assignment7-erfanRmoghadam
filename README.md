# 📚 Book Manager - FastAPI + PostgreSQL + Full CRUD

A simple FastAPI project to **manage, create, search, update, delete** books using **PostgreSQL**  
Giving you the complete **CRUD operations**  
This project uses **raw SQL queries (no ORM)** for database operations and includes a seed script to populate initial book data.

---

## 🚀 Features

### ✅ CRUD Operations

- *Create* a new book with title, author, publisher, and cover image URL
- *Search* books by title, author, or publisher with pagination  
- *Update* book fields (partial update, using patch method)
- *Delete* books from database completely
- *PostgreSQL* integration using raw SQL
- *Seed* script (`seed.py`) to create the table and populate initial data
- Fully *type-checked* with Pydantic models

---


## 📂 Project Structure
```bash
.
├── main.py # FastAPI application
├── seed.py # Script to create the table and insert initial data
├── database.py # Database connection helper
├── requirements.txt # Project dependencies
└── README.md
```
## 🛠 Installation & Running

1. **Clone the repository**

```bash
git clone https://github.com/BackendCourseDocs/assignment7-erfanRmoghadam 
cd path 
```

2. **Create and activate a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt 
```

4. **Setup PostgreSQL**

Create a database named books_db (or update database.py with your DB name)  
Ensure your PostgreSQL username and password match those in database.py

5. **Seed the database**
```bash
python seed.py
```
This will **create** the books table if it does not exist  
And also **populate** it with initial data  
Including up to **50 books** and their author, publisher, cover image URL

## 📌 Running the API

Start the FastAPI server:
```bash
uvicorn main:app --reload
```
Access the API docs at:
```bash
http://127.0.0.1:8000/docs
```

## 📖 API Endpoints

### ➕ Add a Book
```bash
POST /create
```

### 🔍 Search Options
- Search books by title, author, or publisher
```bash
GET /search/book?q=python&page=1&size=3
```
- Search authors and count their books
```bash
GET /search/author?q=martin
```
Returns:  
- Author name  
- Number of books by that author 

### ✏️ Update Book (Partial)
```bash
PATCH /update/book/{id}
```
### 🗑️ Delete Book
```bash
DELETE /delete/book/{id}
```


## 🛡️ Security

All queries use parameterized statements:
```bash
WHERE title ILIKE %s
```
Which prevents SQL Injection attacks.

## 🌱 Database Seeding

seed.py ensures:  
- Table creation
- Initial dataset insertion
- Safe re-run (won't duplicate data)

