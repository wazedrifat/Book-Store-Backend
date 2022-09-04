# from main import app, db
# from fastapi import FastAPI
# from uuid_extensions import uuid7 as uuid
# from typing import List
# from Models.Book import Book, BookDB

# @app.get('/books', response_model = List[Book], status_code = 200)
# def getBooks():
# 	return db.query(BookDB).all()

# @app.get('/book/{bookID}')
# def getBook(BookID: uuid):
# 	pass

# @app.post('/book/create')
# def createBook():
# 	pass

# @app.put('/book/{bookID}/update')
# def updateBook(BookID: uuid):
# 	pass

# @app.delete('/book/{bookID}/delete')
# def deleteBook(BookID: uuid):
# 	pass