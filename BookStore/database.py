from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

Engine = create_engine("postgresql://rygtewxt:FsqBVpXHtQsV69FJM5mcjYPOfbirEnI2@satao.db.elephantsql.com/rygtewxt", echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind = Engine, autocommit = True)