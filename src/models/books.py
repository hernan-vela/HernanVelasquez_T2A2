from init import db, ma, bcrypt, jwt
# unpack information of entities to establish relationships 
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Book(db.Model):
    # name of the table
    __tablename__ = "books"

    # attributes of the table
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    language = db.Column(db.String)
    translator = db.Column(db.String)
    publisher = db.Column(db.String, nullable=False)
    publisher_city = db.Column(db.String)
    publication_date = db.Column(db.Date)
    ebook_isbn = db.Column(db.String, nullable=False)
    print_isbn = db.Column(db.String, nullable=False)

    # relationship between entities book_comments --> books
    book_comments = db.relationship('BookComment', back_populates='book')

    # relationship between entities store_books --> books
    stored_books = db.relationship('StoredBook', back_populates='book')

    # schema for books entity
class BookSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=["user_id", "name", "email"])


    # REVIEW
    # exclusion of 'book' attribute from respective entities
    book_comments = fields.List(fields.Nested('BookCommentSchema', exclude=["book"]))
    # stored_books = fields.List(fields.Nested('StoredBookSchema', exclude=["book"]))

    title = fields.String(required=True, validate=And(Length(min=3, error="Title must be at least 3 characters in length."), Regexp("^[A-Za-z0-9 ]+$", error="Title should start with a capital letter and contain alphanumeric only.")))

    class Meta:
        fields = ("book_id", "title", "author", "language", "translator", "publisher", "publisher_city", "publication_date", "ebook_isbn", "print_isbn","book_comments")

# to handle a single books object
book_schema = BookSchema()

# to handle a list of books objects
books_schema = BookSchema(many=True, exclude=["book_comments"])