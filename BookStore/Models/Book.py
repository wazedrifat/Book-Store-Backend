from pydantic import BaseModel
from uuid import UUID as uuid
from typing import Optional
from ..database import Base
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID, TEXT, BIT, INTEGER, FLOAT, DATE, TIMESTAMP, TIME
from datetime import datetime

class BookDB(Base):
	__tablename__ = 'Book'
	bookID = Column(UUID(as_uuid = True), primary_key = True)
	name = Column(TEXT)
	description = Column(TEXT)
	price = Column(FLOAT)
	rating = Column(FLOAT)
	fileURL = Column(TEXT)
	addedByID = Column(UUID(as_uuid = True))

class Book(BaseModel):
	bookID: uuid
	name: str
	description: str
	price: float
	rating: float
	fileURL: str
	addedByID: uuid

	class Config:
		orm_mode = True