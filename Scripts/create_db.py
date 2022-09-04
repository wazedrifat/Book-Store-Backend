from BookStore.database import Base, Engine
from BookStore.Models.Book import BookDB

Base.metadata.drop_all(Engine)
Base.metadata.create_all(Engine)