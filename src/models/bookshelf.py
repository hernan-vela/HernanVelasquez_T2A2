from init import db, ma, bcrypt, jwt

class Bookshelf(db.Model):
    # Name of the table
    __tablename__ = "bookshelf"

    # Attributes of the table
    bookshelf_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date) # date reading started
    end_date = db.Column(db.Date) # date reading finished
    review = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("user_profile.user_id", nullable = False))

    user = db.relationship('User', back_populates='bookshelf')


    class BookshelfSchema(ma.Schema):
        class Meta:
            fields = ("bookshelf_id", "user_id", "status", "start_date", "end_date", "review")

    # to handle a single bookshelf object
    bookshelf_schema = BookshelfSchema()

    #to handle a list of bookshelf objects
    bookshelfs_schema = BookshelfSchema(many=True)