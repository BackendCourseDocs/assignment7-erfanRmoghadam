import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="books_db",
        user="postgres",
        password="@0110688635"
    )