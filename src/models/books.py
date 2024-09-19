from init import db, ma, bcrypt, jwt
# unpack information of entities to establish relationships 
from marshmallow import fields

class Books(db.Model):
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
    ebook_isbn = db.Column(db.Integer, nullable=False)
    print_isbn = db.Column(db.Integer, nullable=False)

    # definition of 'user_id' as FK in books entity
    user_id = db.Column(db.Integer, db.ForeignKey("user_profile.user_id"), nullable=False)

    # relationship between entities user_profile --> books
    user = db.relationship('User', back_populates='books')

    # relationship between entities book_comments --> books
    book_comment = db.relationship('BookComments', back_populates='books')

    # relationship between entities store_book --> books
    stored_book = db.relationship('StoredBook', back_populates='books')

    # schema for books entity
    class BooksSchema(ma.Schema):
        user = fields.Nested('UserSchema', only=["user_id", "name", "email"])
        
        class Meta:

            # exclusion of 'book' attribute from respective entities
            book_comment = fields.List(fields.Nested('BookCommentsSchema', exclude=["book"]))
            stored_book = fields.List(fields.Nested('StoredBookSchema', exclude=["book"]))
            
            # 'user' or 'user_id'. AAMOD SAYS THAT FK COULD BE EXCLUDED BECAUSE WE HAVE DEFINED 'user' LINK BETWEEN TABLES. TRUE?
            fields = ("book_id", "title", "author", "language", "translator", "publisher", "publisher_city", "publication_date", "ebook_isbn", "print_isbn", "user")

    # to handle a single books object
    book_schema = BooksSchema()

    # to handle a list of books objects
    books_schema = BooksSchema(many=True)