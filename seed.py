from database import get_connection

books = [
    ("Clean Code", "Robert C. Martin", "Prentice Hall", "https://covers.openlibrary.org/b/isbn/9780132350884-L.jpg"),
    ("The Pragmatic Programmer", "Andrew Hunt", "Addison-Wesley", "https://covers.openlibrary.org/b/isbn/9780201616224-L.jpg"),
    ("Introduction to Algorithms", "Thomas H. Cormen", "MIT Press", "https://covers.openlibrary.org/b/isbn/9780262033848-L.jpg"),
    ("Design Patterns", "Erich Gamma", "Addison-Wesley", "https://covers.openlibrary.org/b/isbn/9780201633610-L.jpg"),
    ("Refactoring", "Martin Fowler", "Addison-Wesley", "https://covers.openlibrary.org/b/isbn/9780201485677-L.jpg"),
    ("You Don't Know JS", "Kyle Simpson", "O'Reilly Media", "https://covers.openlibrary.org/b/isbn/9781491904244-L.jpg"),
    ("Eloquent JavaScript", "Marijn Haverbeke", "No Starch Press", "https://covers.openlibrary.org/b/isbn/9781593279509-L.jpg"),
    ("Python Crash Course", "Eric Matthes", "No Starch Press", "https://covers.openlibrary.org/b/isbn/9781593276034-L.jpg"),
    ("Automate the Boring Stuff with Python", "Al Sweigart", "No Starch Press", "https://covers.openlibrary.org/b/isbn/9781593275990-L.jpg"),
    ("Fluent Python", "Luciano Ramalho", "O'Reilly Media", "https://covers.openlibrary.org/b/isbn/9781491946008-L.jpg"),
    ("Learning Python", "Mark Lutz", "O'Reilly Media", "https://covers.openlibrary.org/b/isbn/9781449355739-L.jpg"),
    ("Effective Java", "Joshua Bloch", "Addison-Wesley", "https://covers.openlibrary.org/b/isbn/9780134685991-L.jpg"),
    ("Java Concurrency in Practice", "Brian Goetz", "Addison-Wesley", "https://covers.openlibrary.org/b/isbn/9780321349606-L.jpg"),
    ("Head First Design Patterns", "Eric Freeman", "O'Reilly Media", "https://covers.openlibrary.org/b/isbn/9780596007126-L.jpg"),
    ("Head First Java", "Kathy Sierra", "O'Reilly Media", "https://covers.openlibrary.org/b/isbn/9780596009205-L.jpg"),
    ("Grokking Algorithms", "Aditya Bhargava", "Manning", "https://covers.openlibrary.org/b/isbn/9781617292231-L.jpg"),
    ("Deep Learning", "Ian Goodfellow", "MIT Press", "https://covers.openlibrary.org/b/isbn/9780262035613-L.jpg"),
    ("Hands-On Machine Learning with Scikit-Learn & TensorFlow", "Aurelien Geron", "O'Reilly Media", "https://covers.openlibrary.org/b/isbn/9781491962299-L.jpg"),
    ("Pattern Recognition and Machine Learning", "Christopher Bishop", "Springer", "https://covers.openlibrary.org/b/isbn/9780387310732-L.jpg"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "Pearson", "https://covers.openlibrary.org/b/isbn/9780136042594-L.jpg"),
    ("Computer Networking: A Top-Down Approach", "James Kurose", "Pearson", "https://covers.openlibrary.org/b/isbn/9780133594140-L.jpg"),
    ("Operating System Concepts", "Abraham Silberschatz", "Wiley", "https://covers.openlibrary.org/b/isbn/9781118063330-L.jpg"),
    ("Modern Operating Systems", "Andrew S. Tanenbaum", "Pearson", "https://covers.openlibrary.org/b/isbn/9780133591620-L.jpg"),
    ("Computer Organization and Design", "David Patterson", "Morgan Kaufmann", "https://covers.openlibrary.org/b/isbn/9780124077263-L.jpg"),
    ("Clean Architecture", "Robert C. Martin", "Prentice Hall", "https://covers.openlibrary.org/b/isbn/9780134494166-L.jpg"),
    ("Domain-Driven Design", "Eric Evans", "Addison-Wesley", "https://covers.openlibrary.org/b/isbn/9780321125217-L.jpg"),
    ("Building Microservices", "Sam Newman", "O'Reilly Media", "https://covers.openlibrary.org/b/isbn/9781491950357-L.jpg"),
    ("Site Reliability Engineering", "Betsy Beyer", "O'Reilly Media", "https://covers.openlibrary.org/b/isbn/9781491929124-L.jpg"),
    ("Docker Deep Dive", "Nigel Poulton", "Independently published", "https://covers.openlibrary.org/b/isbn/9781521822807-L.jpg"),
    ("Kubernetes Up and Running", "Kelsey Hightower", "O'Reilly Media", "https://covers.openlibrary.org/b/isbn/9781491935671-L.jpg"),
    ("Linux Command Line", "William Shotts", "No Starch Press", "https://covers.openlibrary.org/b/isbn/9781593273897-L.jpg"),
    ("How Linux Works", "Brian Ward", "No Starch Press", "https://covers.openlibrary.org/b/isbn/9781593275679-L.jpg"),
    ("The Art of Computer Programming", "Donald Knuth", "Addison-Wesley", "https://covers.openlibrary.org/b/isbn/9780201896831-L.jpg"),
    ("Code Complete", "Steve McConnell", "Microsoft Press", "https://covers.openlibrary.org/b/isbn/9780735619678-L.jpg"),
    ("The Mythical Man-Month", "Frederick P. Brooks Jr.", "Addison-Wesley", "https://covers.openlibrary.org/b/isbn/9780201835953-L.jpg"),
    ("Working Effectively with Legacy Code", "Michael Feathers", "Prentice Hall", "https://covers.openlibrary.org/b/isbn/9780131177055-L.jpg"),
    ("Programming Pearls", "Jon Bentley", "Addison-Wesley", "https://covers.openlibrary.org/b/isbn/9780201657883-L.jpg"),
    ("Structure and Interpretation of Computer Programs", "Harold Abelson", "MIT Press", "https://covers.openlibrary.org/b/isbn/9780262510875-L.jpg"),
    ("Compilers: Principles, Techniques, and Tools", "Alfred Aho", "Pearson", "https://covers.openlibrary.org/b/isbn/9780321486813-L.jpg"),
    ("Computer Graphics: Principles and Practice", "John F. Hughes", "Addison-Wesley", "https://covers.openlibrary.org/b/isbn/9780321399526-L.jpg"),
    ("Real-Time Rendering", "Tomas Akenine-Moller", "A K Peters", "https://covers.openlibrary.org/b/isbn/9781568814247-L.jpg"),
    ("Game Engine Architecture", "Jason Gregory", "CRC Press", "https://covers.openlibrary.org/b/isbn/9781138035454-L.jpg"),
    ("AI for Games", "Ian Millington", "CRC Press", "https://covers.openlibrary.org/b/isbn/9780123747310-L.jpg"),
    ("Unity in Action", "Joe Hocking", "Manning", "https://covers.openlibrary.org/b/isbn/9781617294969-L.jpg"),
    ("Learning React", "Alex Banks", "O'Reilly Media", "https://covers.openlibrary.org/b/isbn/9781492051725-L.jpg"),
    ("Fullstack Vue", "Hassan Djirdeh", "Fullstack.io", "https://covers.openlibrary.org/b/isbn/9780991344628-L.jpg"),
    ("HTML and CSS: Design and Build Websites", "Jon Duckett", "Wiley", "https://covers.openlibrary.org/b/isbn/9781118008188-L.jpg"),
    ("JavaScript: The Good Parts", "Douglas Crockford", "O'Reilly Media", "https://covers.openlibrary.org/b/isbn/9780596517748-L.jpg"),
    ("Secrets of the JavaScript Ninja", "John Resig", "Manning", "https://covers.openlibrary.org/b/isbn/9781617292859-L.jpg")
]

def create_table():
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100),
            author VARCHAR(100),
            publisher VARCHAR(100),
            image_url TEXT );
""")
    
    con.commit()
    cur.close()
    con.close()
    print("table 'books' ensured.")

def seed():
    con = get_connection()
    cur = con.cursor()

    create_table()

    cur.execute("SELECT COUNT(*) FROM books;")
    count = cur.fetchone()[0]

    if count > 0:
        print("Database has data already.")
        con.close()
        return

    cur.executemany("""
        INSERT INTO books (title, author, publisher, image_url)
        VALUES (%s, %s, %s, %s);
    """, books)

    con.commit()
    con.close()
    print("Data inserted successfully.")

if __name__ == "__main__":
    seed()
