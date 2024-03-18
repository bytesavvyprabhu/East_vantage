from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

def test_add_book():
    book_data = {"title": "LEarn AI", "author": "PRABHu", "publication_year": 2022}
    response = client.post("/books/", json=book_data)
    
    #check condition if it is 200 or not ?
    assert response.status_code == 200
    
    # check whether data is matching or not 
    assert response.json() == book_data


def test_get_books():
    response = client.get("/books/")
    
    # check condition if it is 200 or not ?
    assert response.status_code == 200
    
    assert isinstance(response.json(), list)
    for book in response.json():
        assert isinstance(book, dict)

def test_add_review():
    review_data = {"book_id": 1, "review_text": "Wawoo Such a nice book", "rating":10}
    response = client.post("/reviews/", json=review_data)
    assert response.status_code == 200
    assert response.json() == review_data

@pytest.mark.parametrize("book_id", [1, 2, 3])    
def test_get_review(book_id):
    response = client.get("/reviews/{book_id}")
    assert response.status_code == 200
