from fastapi import FastAPI, status, HTTPException
from BookStore.database import SessionLocal
from typing import List
from BookStore.Models.Book import Book, BookDB
from uuid import UUID as uuid

app = FastAPI()

db = SessionLocal()

@app.get('')
def index():
	return 'Home Page'



@app.get('/books', response_model = List[Book], status_code = status.HTTP_200_OK)
def getBooks():
	return db.query(BookDB).all()

@app.get('/book/{bookID}', response_model = Book, status_code = status.HTTP_200_OK)
def getBook(bookID: uuid):
	return db.query(BookDB).filter(BookDB.bookID == bookID).first()

@app.post('/book/create', response_model = Book, status_code = status.HTTP_201_CREATED)
def createBook(book: Book):
	if (getBook(book.bookID)):
		raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "book already exists")

	bookDB = BookDB(
		bookID = book.bookID,
		name = book.name,
		description = book.description,
		price = book.price,
		rating = book.rating,
		fileURL = book.fileURL,
		addedByID = book.addedByID
	)
	db.add(bookDB)
	return bookDB

@app.put('/book/{bookID}/update', response_model = Book, status_code = status.HTTP_200_OK)
def updateBook(bookID: uuid, newBook: Book):
	book = getBook(bookID)
	book.bookID = newBook.bookID
	book.name = newBook.name
	book.description = newBook.description
	book.price = newBook.price
	book.rating = newBook.rating
	book.fileURL = newBook.fileURL
	book.addedByID = newBook.addedByID
	return book


@app.delete('/book/{bookID}/delete', status_code = status.HTTP_200_OK)
def deleteBook(bookID: uuid):
	book = getBook(bookID)

	if (book is None):
		raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "book does not exists")
	db.delete(book)

