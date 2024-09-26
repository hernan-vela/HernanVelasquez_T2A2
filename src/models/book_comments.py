from init import db, ma, bcrypt, jwt
# unpack information of entities to establish relationships 
from marshmallow import fields

class BookComment(db.Model):
    # name of the table
    __tablename__ = "book_comments"

    # attributes of the table
    book_comment_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    comment = db.Column(db.Text, nullable=False)

    # definition of 'user_id' as FK in 'book_comments' entity for 'users_profiles' entity
    user_id = db.Column(db.Integer, db.ForeignKey("users_profiles.user_id"),nullable=False)

    #definition of 'book_id' as a FK in 'book_comments' entity for 'books' entity
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id"),nullable=False)

    # relationship between entities 'users_profiles' --> 'book_comments'
    user = db.relationship('User', back_populates='book_comments')

    # relationship between entities 'books' --> 'book_comments'
    book = db.relationship('Book', back_populates='book_comments')

# schema to get comments of one book
class BookCommentSchema(ma.Schema):
    # IS THIS CORRECT? WILL IT FETCH A LIST OF COMMENTS OF ONE USER?
    user = fields.Nested('UserSchema', only=["user_id", "user_name"])
    book = fields.List(fields.Nested('BookSchema', only=["book_id", "title", "author"]))

    class Meta:
        fields = ("user", "book", "book_comment_id", "date", "comment")

# to handle a single 'book_comments' object
book_comment_schema = BookCommentSchema()

# to handle a list of 'book_comments' objects
book_comments_schema = BookCommentSchema(many=True)


# schema to get all comments of a user
class BookCommentsUserSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=["user_id", "user_name"])
    book = fields.List(fields.Nested('BookSchema', only=["book_id", "title", "author"]))

    class Meta:
        fields = ("user", "book", "book_comment_id", "date", "comment")

# to handle a single 'book_comments' object
book_comment_schema = BookCommentsUserSchema()

# to handle a list of 'book_comments' objects
book_comments_schema = BookCommentsUserSchema(many=True)

