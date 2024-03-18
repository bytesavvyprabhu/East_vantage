from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List
from db import conn, c
import sqlite3
from model import Book, Review, BookList, ReviewList

app = FastAPI()
conn = sqlite3.connect('book_reviews.db')
c = conn.cursor()


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Book Review System API"}

@app.post("/books/", response_model=Book)
async def add_book(book: Book):
    c.execute("INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)", (book.title, book.author, book.publication_year))
    conn.commit()
    conn.close()
    return book

@app.post("/reviews/", response_model=Review)
async def submit_review(review: Review):
    c.execute(f"INSERT INTO reviews (book_id, review_text, rating) VALUES (?, ?, ?))",(review.book_id,review.review_text,review.rating))
    conn.commit()
    conn.close()
    return review

@app.get("/books/", response_model=BookList)
async def get_books(author: str = None, publication_year: int = None):
    if author:
        c.execute(f"SELECT * FROM books WHERE author={author}")
    elif publication_year:
        c.execute(f"SELECT * FROM books WHERE publication_year={publication_year}")
    else:
        c.execute("SELECT * FROM books")
    books = c.fetchall()
    conn.close()
    return {"books": books}

@app.get("/reviews/{book_id}", response_model=ReviewList)
async def get_reviews(book_id: int):
    c.execute(f"SELECT * FROM reviews WHERE book_id={book_id}")
    reviews = c.fetchall()
    conn.close()
    return {"reviews": reviews}

# Background Task
def send_confirmation_email(email: str, message: str):
    print(f"Sending email to {email}: {message}")

@app.post("/submit-review/")
async def submit_review_and_send_confirmation(review: Review, background_tasks: BackgroundTasks):
    email = "example@example.com" #ENter Email ID.
    message = "Your review has been submitted successfully."
    background_tasks.add_task(send_confirmation_email, email, message)
    return {"message": "Review submitted successfully and confirmation email will be sent shortly."}
