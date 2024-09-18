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

class UserSchema(ma.Schema):
    class Meta:
        bookshelf = fields.List(fields.Nested('BookshelfSchema', exclude=["user"]))
        fields = ("user_id", "name", "email", "user_name", "password", "is_admin", "bookshelf")

# to handle a single user object
user_schema = UserSchema(exclude=["password"])

# to handle a list of user objects
users_schema = UserSchema(many=True, exclude=["password"])