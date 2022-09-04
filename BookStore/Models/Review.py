# from click import option
# from pydantic import BaseModel
# from uuid_extensions import uuid7 as uuid
# from typing import Optional
# from database import Base
# from sqlalchemy import Column, String, Boolean, Integer, Float

# class Review(Base):
# 	__tabname__ = 'Review'

# 	reviewID: uuid
# 	rating: float
# 	reviewerID: uuid
# 	reviewMessage: Optional[str]
# 	likes: int = 0