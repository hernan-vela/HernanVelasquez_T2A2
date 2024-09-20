from init import db, ma, bcrypt, jwt
# unpack information of entities to establish relationships 
from marshmallow import fields

class Bookshelf(db.Model):
    # name of the table
    __tablename__ = "bookshelves"

    # attributes of the table
    bookshelf_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date) # date reading started
    end_date = db.Column(db.Date) # date reading finished
    review = db.Column(db.String)

    # definition of 'user_id' as FK in 'bookshelf' entity
    user_id = db.Column(db.Integer, db.ForeignKey("users_profiles.user_id"),nullable = False)

    # relationship between entities 'users_profiles' --> 'bookshelf'
    user = db.relationship('User', back_populates='bookshelves')
    
    # relationship between entities 'stored_book' --> 'bookshelf'
    stored_books = db.relationship('StoredBook', back_populates='bookshelf')

# schema for 'bookshelf' entity
class BookshelfSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=["user_id", "name", "email"])
    
    # exclusion of 'bookshelf' attribute from 'stored_book'
    stored_books = fields.List(fields.Nested('StoredBookSchema', exclude=["bookshelf"]))

    class Meta:
        fields = ("bookshelf_id", "status", "start_date", "end_date", "review", "user", "stored_books")

# to handle a single 'bookshelf' object
bookshelf_schema = BookshelfSchema()

#to handle a list of 'bookshelf' objects
bookshelves_schema = BookshelfSchema(many=True)