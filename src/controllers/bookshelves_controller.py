from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.books import Book
from models.bookshelves import Bookshelf, bookshelf_user_schema, bookshelves_user_schema
from models.stored_books import StoredBook


bookshelves_bp = Blueprint("bookshelves", __name__, url_prefix="/bookshelves")

# GET - fetch all books in a bookshelf of any user
@bookshelves_bp.route("/<int:bookshelf_id>")
@jwt_required()
def get_a_bookshelf(bookshelf_id):

    # filter 'bookshelves' entity to find the bookshelf_id
    stmt = db.select(Bookshelf).filter_by(bookshelf_id=bookshelf_id)
    bookshelf = db.session.scalar(stmt)

    if bookshelf:
        return bookshelf_user_schema.dump(bookshelf)
    else:
        return {"error": f"Bookshelf {bookshelf_id} does not exist"}, 404


# POST - add a book to a specific bookshelf
@bookshelves_bp.route("/<int:bookshelf_id>/books/<int:book_id>", methods=["POST"])
@jwt_required()
def add_book_to_bookshelf(bookshelf_id, book_id):
    # check if the authenticated user owns the bookshelf
    user = get_jwt_identity()

    # fetch the bookshelf to check existence and ownership
    stmt = db.select(Bookshelf).filter_by(user_id=user, bookshelf_id=bookshelf_id)
    bookshelf_owned = db.session.scalar(stmt)

    # nice message if not existence, or ownership
    if not bookshelf_owned:
        return {"message": "Bookshelf not found or not owned by the user."}, 404

    # get the data to store from the request body
    body_data = request.get_json()

    # check if book_id already exists in the given bookshelf
    stmt = db.select(StoredBook).filter_by(bookshelf_id=bookshelf_id, book_id=book_id)
    existing_book = db.session.scalar(stmt)

    # if the book_id exists, return a message
    if existing_book:
        return {"message": f"Book {book_id} already exists in bookshelf {bookshelf_id}"}, 400

    # add the book to the bookshelf
    storedBook = StoredBook(
        book_id=book_id,
        bookshelf_id=bookshelf_id,
        start_date=body_data.get("start_date"),
        end_date=body_data.get("end_date")
    )

    # add book to the bookshelf and commit changes
    db.session.add(storedBook)
    db.session.commit()

    return {"message": f"Book {book_id} added successfully to bookshelf {bookshelf_id}!"}, 201


# DELETE - remove a book from a specific bookshelf
@bookshelves_bp.route("/<int:bookshelf_id>/books/<int:book_id>", methods=["DELETE"])
@jwt_required()
def delete_book_in_bookshelf(bookshelf_id, book_id):
    # check if the authenticated user owns the bookshelf
    user = get_jwt_identity()

    # fetch the bookshelf to check existence and ownership
    stmt = db.select(Bookshelf).filter_by(user_id=user, bookshelf_id=bookshelf_id)
    bookshelf_owned = db.session.scalar(stmt)

    # nice message if not existence, or ownership
    if not bookshelf_owned:
        return {"message": "Bookshelf not found or not owned by the user."}, 404

    # fetch the bookshelf from the database
    stmt = db.select(StoredBook).filter_by(bookshelf_id=bookshelf_id, book_id=book_id)
    storedBook = db.session.scalar(stmt)
    
    # if bookshelf exists
    if storedBook:
        db.session.delete(storedBook)
        db.session.commit()
        return {"message": f"Book {book_id} deleted succesfully from bookshelf {bookshelf_id}!"}
    # else
    else:
        #return error message
        return {"error": f"Book {book_id} coudln't be found in bookshelf {bookshelf_id}"}, 404


