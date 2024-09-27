from init import db, ma, bcrypt, jwt
# 'fields' unpack information of entities to establish relationships 
from marshmallow import fields
from marshmallow.validate import OneOf

VALID_STATUSES = ("Read", "Reading", "To-read")

class Bookshelf(db.Model):
    # name of the table
    __tablename__ = "bookshelves"

    # attributes of the table
    bookshelf_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String, nullable=False)

    # definition of 'user_id' as FK in 'bookshelf' entity
    user_id = db.Column(db.Integer, db.ForeignKey("users_profiles.user_id"),nullable = False)

    # relationship between entities 'users_profiles' --> 'bookshelf'
    user = db.relationship('User', back_populates='bookshelves')
    
    # relationship between entities 'stored_book' --> 'bookshelf'
    stored_books = db.relationship('StoredBook', back_populates='bookshelf')


# schema to fetch bookshelves of a user
class BookshelfUserSchema(ma.Schema):

    user = fields.Nested('UserSchema', only=["user_id", "user_name"])
    stored_books = fields.List(fields.Nested('StoredBookSchema', only=["book"])) 

    status = fields.String(required=True, validate=OneOf(VALID_STATUSES))

    class Meta:
        fields = ("user", "bookshelf_id", "status", "stored_books")

# to handle a single 'bookshelf' object
bookshelf_user_schema = BookshelfUserSchema()

#to handle a list of 'bookshelf' objects
bookshelves_user_schema = BookshelfUserSchema(many=True)