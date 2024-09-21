from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.stored_books import StoredBook, stored_book_schema, stored_books_schema

stored_books_bp = Blueprint("stored_book", __name__, url_prefix="/stored_book")

# DOES THIS OPERATION MAKE SENSE? WILL THIS GIVE ME ALL THE BOOKSHELVES OF ALL THE USERS IN THE SYSTEM?
# /stored_book - GET - fetch all stored_book
@stored_books_bp.route("/")
def get_all_stored_books():
    stmt = db.select(StoredBook)
    stored_books = db.session.scalars(stmt)
    return stored_books_schema.dump(stored_books)
# /stored_book/<id> - GET - fetch a specific stored_book
@stored_books_bp.route("/<int:stored_book_id>")
def get_a_stored_book(stored_book_id):
    stmt = db.select(StoredBook).filter_by(id=stored_book_id)
    stored_book = db.session.scalar(stmt)
    if stored_book:
        return stored_book_schema.dump(stored_book)
    else:
        return {"error": f"Stored_book with id {stored_book_id} does not exist"}, 404

#CREATE....DOES THIS FUNCTION MAKE SENSE HERE?
# /stored_book - POST - create a new stored_book
    # get the data from the body of the request
    # create a new stored_book model instance
    # add and commit to stored_book
	# return acknowledgement message
    # ackonwledgement message

# /stored_book/<id> - DELETE - delete a stored_book
@stored_books_bp.route("/<int:stored_book_id>", methods=["DELETE"])
@jwt_required()
def delete_stored_book(stored_book_id):
    # fetch the stored_book from books_shelves
    stmt = db.select(StoredBook).filter_by(id=stored_book_id)
    stored_book = db.session.scalar(stmt)
    # if stored_book exists
    if stored_book:
        # delete the stored_book
        db.session.delete(stored_book)
        db.session.commit()
        return {"message": f"Stored_book {stored_book.stored_book_id} deleted successfully!"}
    # else
    else:
        # return error message
        return{"error": f"Stored_book with id {stored_book_id} does not exist"}, 404

#UPDATE....DOES THIS FUNCTION MAKE SENSE HERE?
# /stored_book/<id> - PUT, PATCH - edit a stored_book entry
    # get the info from the body of the request
    # get the stored_book from books_shelves
    # if the stored_book exists
        # update the field as required
        # commit to books_shelves
        # return acknowledgement message
    # else
        # return an error message