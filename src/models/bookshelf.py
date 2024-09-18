from init import db, ma, bcrypt, jwt
# unpack information of entities to establish relationships 
from marshmallow import fields

class Bookshelf(db.Model):
    # name of the table
    __tablename__ = "bookshelf"

    # attributes of the table
    # HOW CAN I TELL HERE WHAT BOOK AN ENTRY IS REFERRING TO?
    bookshelf_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date) # date reading started
    end_date = db.Column(db.Date) # date reading finished
    review = db.Column(db.String)

    # definition of 'user_id' as FK in bookshelf entity
    user_id = db.Column(db.Integer, db.ForeignKey("user_profile.user_id", nullable = False))

    # relationship between entities user_profile --> bookshelf
    user = db.relationship('User', back_populates='bookshelf')

    # schema for bookshelf entity
    class BookshelfSchema(ma.Schema):
        user = fields.Nested('UserSchema', only=["user_id", "name", "email"])
        class Meta:
            # 'user' or 'user_id'. AAMOD SAYS THAT FK COULD BE EXCLUDED BECAUSE WE HAVE DEFINED 'user' LINK BETWEEN TABLES. TRUE?
            fields = ("bookshelf_id", "title", "status", "start_date", "end_date", "review", "user")

    # to handle a single bookshelf object
    bookshelf_schema = BookshelfSchema()

    #to handle a list of bookshelf objects
    bookshelfs_schema = BookshelfSchema(many=True)