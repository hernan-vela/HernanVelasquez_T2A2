from init import db, ma, bcrypt, jwt
# unpack information of entities to establish relationship
from marshmallow import fields
from marshmallow.validate import Regexp

class User(db.Model):
    # Name of the table
    __tablename__ = "users_profiles"

    # Attributes of the table
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    user_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # relationship between entities 'bookshelf' --> 'users_profiles'
    bookshelves = db.relationship('Bookshelf', back_populates='user')
    # relationship between entities 'book_comments' --> 'users_profiles'
    book_comments = db.relationship('BookComment', back_populates='user')

class UserSchema(ma.Schema):
    # exclusion of 'user' attribute from respective entities
    bookshelves = fields.List(fields.Nested('BookshelfSchema', exclude=["user"]))
    book_comments = fields.List(fields.Nested('BookCommentSchema', exclude=["user"]))

    # validation of email according to format
    email = fields.String(required=True, validate=Regexp("^\S+@\S+\.\S+$", error="Invalid email Format."))

    class Meta:
        fields = ("user_id", "name", "email", "user_name", "password", "is_admin", "bookshelves", "book_comments")

# to handle a single user object
user_schema = UserSchema(exclude=["password"])

# to handle a list of user objects
users_schema = UserSchema(many=True, exclude=["password"])