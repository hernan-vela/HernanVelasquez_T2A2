from init import db, ma, bcrypt, jwt
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
    bookshelves = db.relationship('Bookshelf', back_populates='user', cascade="all, delete")
    # relationship between entities 'book_comments' --> 'users_profiles'
    book_comments = db.relationship('BookComment', back_populates='user')

class UserSchema(ma.Schema):
    # exclusion of 'user' attribute from respective entities
    book_comments = fields.List(fields.Nested('BookCommentSchema', exclude=["user"]))

    # validation of email according to format
    email = fields.String(required=True, validate=Regexp("^\S+@\S+\.\S+$", error="Invalid email Format."))

    class Meta:
        fields = ("user_id", "name", "email", "user_name", "password", "is_admin", "book_comments")

# to handle a single user object
user_schema = UserSchema(only=["user_id", "name", "user_name"])

# to handle a list of user objects
users_schema = UserSchema(many=True, only=["user_id", "user_name"])


class AllUserSchema(ma.Schema):

    # validation of email according to format
    email = fields.String(required=True, validate=Regexp("^\S+@\S+\.\S+$", error="Invalid email Format."))

    class Meta:
        fields = ("user_id", "name", "email", "user_name", "password", "is_admin")


# to handle a list of user objects
all_users_schema = AllUserSchema(many=True, only=["user_id", "name", "email"])