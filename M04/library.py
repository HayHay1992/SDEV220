from library import Library
app = library(__name__)
from library_sqlalchemy import book_library

Base = book_library()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    book_name = Column(String)
    author = Column(Integer)
    publisher = Column(Date)
