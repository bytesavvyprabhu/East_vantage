import sqlite3

conn = sqlite3.connect('book_reviews.db')
c = conn.cursor()

# Create tables if not exist
c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, publication_year INTEGER)''')
c.execute('''CREATE TABLE IF NOT EXISTS reviews
             (id INTEGER PRIMARY KEY AUTOINCREMENT, book_id INTEGER, review_text TEXT, rating INTEGER)''')


