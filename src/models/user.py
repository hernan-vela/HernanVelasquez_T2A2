from init import db, ma, bcrypt, jwt
# unpack information of entities to establish relationship
from marshmallow import fields

class User(db.Model):
    # Name of the table
    __tablename__ = "user_profile"

    # Attributes of the table
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    user_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

# relationship between entities 'bookshelf' --> 'user_profile'
    bookshelf = db.relationship('Bookshelf', back_populates='user_profile')

# relationship between entities 'books' --> 'user_profile'
    books = db.relationship('Books', back_populates='user_profile')

# relationship between entities 'book_comments' --> 'user_profile'
    book_comments = db.relationship('BookComments', back_populates='user_profile')

class UserSchema(ma.Schema):
    class Meta:

        # exclusion of 'user' attribute from respective entities
        bookshelf = fields.List(fields.Nested('BookshelfSchema', exclude=["user"]))
        book = fields.List(fields.Nested('BooksSchema', exclude=["user"]))
        book_comment = fields.List(fields.Nested('BookCommentsSchema', exclude=["user"]))

        # IS IT COHERENT THESE FIELDS IN THE user MODEL? AREN'T THEY TOO MANY?
        fields = ("user_id", "name", "email", "user_name", "password", "is_admin", "bookshelf", "book", "book_comment")

# to handle a single user object
user_schema = UserSchema(exclude=["password"])

# to handle a list of user objects
users_schema = UserSchema(many=True, exclude=["password"])