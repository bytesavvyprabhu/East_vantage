from pydantic import BaseModel
from typing import List

class Book(BaseModel):
    title: str
    author: str
    publication_year: int

class Review(BaseModel):
    book_id: int
    review_text: str
    rating: int

class BookList(BaseModel):
    books: List[Book]

class ReviewList(BaseModel):
    reviews: List[Review]
