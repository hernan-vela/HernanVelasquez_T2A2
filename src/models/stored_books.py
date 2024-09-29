from init import db, ma, bcrypt, jwt
from marshmallow import fields

class StoredBook(db.Model):
    # name of the table
    __tablename__ = "stored_books"

    # attributes of the table
    stored_book_id = db.Column(db.Integer, primary_key=True)
    
    # definition of 'book_id' as FK in 'stored_book' entity for 'books' entity
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id"), nullable=False)

    # definition of 'bookshelf_id' as FK in 'stored_book' entity for 'bookshelf' entity
    bookshelf_id = db.Column(db.Integer, db.ForeignKey("bookshelves.bookshelf_id"), nullable=False)

    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    # relationship between entities 'book' --> 'stored_books'
    book = db.relationship('Book', back_populates='stored_books')

    # relationship between entities 'bookshelf' --> 'stored_books'
    bookshelf = db.relationship('Bookshelf', back_populates='stored_books')

class StoredBookSchema(ma.Schema):
    book = fields.Nested('BookSchema', only=["book_id", "title", "author"])
    bookshelf = fields.Nested('BookshelfUserSchema', only=["bookshelf_id", "user", "status"])

    class Meta:
        fields = ("stored_book_id", "book", "bookshelf")

 # to handle a single 'stored_book' object
stored_book_schema = StoredBookSchema()

    #to handle a list of 'stored_book' objects
stored_books_schema = StoredBookSchema(many=True)