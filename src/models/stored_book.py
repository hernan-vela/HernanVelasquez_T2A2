from init import db, ma, bcrypt, jwt
# unpack information of entities to establish relationships 
from marshmallow import fields

class StoredBook(db.Model):
    # name of the table
    __tablename__ = "stored_book"

    # attributes of the table
    stored_book_id = db.Column(db.Integer, primary_key=True)
    
    # definition of 'book_id' as FK in 'stored_book' entity for 'books' entity
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id", nullable=False))

    # definition of 'bookshelf_id' as FK in 'stored_book' entity for 'bookshelf' entity
    bookshelf_id = db.Column(db.Integer, db.ForeignKey("bookshelf.bookshelf_id", nullable=False))

    # relationship between entities 'books' --> 'stored_book'
    book = db.relationship('Books', back_populates='stored_book')

    # relationship between entities 'bookshelf' --> 'stored_book'
    bookshelf = db.relationship('Bookshelf', back_populates='stored_book')

    class StoredBookSchema(ma.Schema):
        # IF TITLE IS ALREADY FETCHED FROM book SHOULD I RETRIEVE TITLE FROM bookshelf AS WELL?
        book = fields.Nested('BookSchema', only=["book_id", "title", "author"])
        bookshelf = fields.Nested('BookshelfSchema', only=["bookshelf_id", "user_id", "status"])

        class Meta:
            # 'user' or 'user_id'. AAMOD SAYS THAT FK COULD BE EXCLUDED BECAUSE WE HAVE DEFINED 'user' LINK BETWEEN TABLES. TRUE?
            fields = ("stored_book_id", "book", "bookshelf")

 # to handle a single 'stored_book' object
    stored_book_schema = StoredBookSchema()

    #to handle a list of 'stored_book' objects
    stored_books_schema = StoredBookSchema(many=True)