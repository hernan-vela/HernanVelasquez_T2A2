from init import db, ma, bcrypt, jwt
# unpack information of entities to establish relationships 
from marshmallow import fields

class BookComments(db.Model):
    # name of the table
    __tablename__ = "book_comments"

    # attributes of the table
    book_comment_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)

    # definition of 'user_id' as FK in 'book_comments' entity for 'user_profile' entity
    user_id = db.Column(db.Integer, db.ForeignKey("user_profile.user_id", nullable=False))

    #definition of 'book_id' as a FK in 'book_comments' entity for 'books' entity
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id", nullable=False))

    # relationship between entities 'user_profile' --> 'book_comments'
    user = db.relationship('User', back_populates='book_comments')

    # relationship between entities 'books' --> 'book_comments'
    book = db.relationship('Books', back_populates='books')

# schema for 'book_comments'
class BookCommentsSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=["user_id", "name", "email"])
    book = fields.Nested('BooksSchema', only=["book_id", "title", "author"])

    class Meta:
        # BY SPECIFYING THESE FIELDS AND WITH THE SCHEMA DEFINITION, IS IT ENOUGH TO DECLARE WHAT BOOK THE COMMENT REFERS TO? 
        fields = ("book_comment_id", "comment", "user", "book")

# to handle a single 'book_comments' object
book_comment_schema = BookCommentsSchema()

# to handle a list of 'book_comments' objects
book_comments_schema = BookCommentsSchema(many=True)