from init import db, ma, bcrypt, jwt
# unpack information of entities to establish relationships 
from marshmallow import fields, validates
from marshmallow.validate import OneOf
from marshmallow.exceptions import ValidationError

VALID_STATUSES = ("Read", "Reading", "To-read")

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

    # definition of 'user_id' as FK in 'bookshelf' entity
    user_id = db.Column(db.Integer, db.ForeignKey("user_profile.user_id", nullable = False))

    # relationship between entities 'user_profile' --> 'bookshelf'
    user = db.relationship('User', back_populates='bookshelf')
    
    # relationship between entities 'stored_book' --> 'bookshelf'
    stored_book = db.relationship('StoredBook', back_populates='bookshelf')

    # schema for 'bookshelf' entity
    class BookshelfSchema(ma.Schema):
        user = fields.Nested('UserSchema', only=["user_id", "name", "email"])

        status = fields.String(validate=OneOf(VALID_STATUSES))

        @validates("status")
        def validate_status(self, value):
        # if trying to see the value of status as "Read"
            if value == VALID_STATUSES[0]:
                # check whether an existing 'Read' book exists or not
                # SELECT COUNT(*) FROM bookshelf WHERE status="Read"
                    stmt = db.select(db.func.count()).select_from(Bookshelf).filter_by(status=VALID_STATUSES[0])
                    count = db.session.scalar(stmt)
                    # if it exists
                    if count > 0:
                        # send error message
                        raise ValidationError("You already have read this book.")

        class Meta:

            # exclusion of 'bookshelf' attribute from 'stored_book'
            stored_book = fields.List(fields.Nested('StoredBookSchema', exclude=["bookshelf"]))

            # 'user' or 'user_id'. AAMOD SAYS THAT FK COULD BE EXCLUDED BECAUSE WE HAVE DEFINED 'user' LINK BETWEEN TABLES. TRUE?
            fields = ("bookshelf_id", "title", "status", "start_date", "end_date", "review", "user")

    # to handle a single 'bookshelf' object
    bookshelf_schema = BookshelfSchema()

    #to handle a list of 'bookshelf' objects
    bookshelves_schema = BookshelfSchema(many=True)