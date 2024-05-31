# You are required to build a simple CRUD (Create, Read, Update, Delete) API for managing a collection of books. 
# Create a new book: Users should be able to add a new book to the collection by providing details
#  such as title, author, publication year, and genre.

from fastapi import FastAPI, Body

app = FastAPI()

from pydantic import BaseModel
from typing import Annotated

# schema for the book details
class BookDetails(BaseModel):
    Title:str
    Author: str
    Publication_year:int
    Genre:str
    ID:int
    
# to create a new book
@app.post("/create-a-book")
def create_new_book(details:BookDetails):
    return{"message":"New book created Successfully!Bravo"}

#  Retrieve a list of all books: Users should be able to retrieve a list of all books in the collection
# Read all books
@app.get("/all_books")
def get_all_books(books:BookDetails):
    return {"data":books}


#- Retrieve details of a specific book: Users should be able to retrieve details of a specific book by providing its unique identifier (ID).
@app.get("/specific_book/{ID}") 
def get_a_specific_book(ID):
    return { "ID" :ID}

# Update details of a book: Users should be able to update details of a specific book by providing its unique identifier (ID) and the updated information.
@app.post("/books/{ID}")
def update_book(ID: Annotated[int,Body()]):
    return {"message":"book updated succefully by ID"}

# - Delete a book: Users should be able to delete a specific book from the collection by providing its unique identifier (ID).
@app.delete("/books/{ID}")
def delete_book(ID: int):
    return {"message": "Book deleted"}

    