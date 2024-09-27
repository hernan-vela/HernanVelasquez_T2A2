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
def get_a_bookshelf(bookshelf_id):
    stmt = db.select(Bookshelf).filter_by(bookshelf_id=bookshelf_id)

    #db.select(Book).join(StoredBook).where(StoredBook.bookshelf_id==bookshelf_id, Book.book_id==StoredBook.book_id)

    bookshelf = db.session.scalar(stmt)
    return bookshelf_user_schema.dump(bookshelf)

# GET - fetch all the bookshelves of a user
# @bookshelves_bp.route("/")
# @jwt_required()
# def get_bookshelves():
#     user_id = get_jwt_identity()
#     stmt = db.select(Bookshelf).filter_by(user_id=user_id)
#     bookshelves = db.session.scalar(stmt)
#     if bookshelves:
#         return bookshelves_user_schema.dump(bookshelves)
#     else:
#         return {"error": f"Bookshelves of user {user_id} cannot be found or user does not exist"}, 404
    

# DELETE - remove a book from a specific bookshelf
@bookshelves_bp.route("/<int:bookshelf_id>/books/<int:book_id>", methods=["DELETE"])
@jwt_required()
def delete_book_in_bookshelf(bookshelf_id, book_id):
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

# POST - add a book to a specific bookshelf
@bookshelves_bp.route("/<int:bookshelf_id>/books/<int:book_id>", methods=["POST"])
@jwt_required()
def add_book_to_bookshelf(bookshelf_id, book_id):
    # get the data to store from the request body
    body_data = request.get_json()
    # fetch the bookshelf from the database
    stmt = db.select(Bookshelf).filter_by(bookshelf_id=bookshelf_id)
    bookshelf = db.session.scalar(stmt)
    # if bookshelf exists
    if bookshelf:
        # add the book to the bookshelf
        storedBook = StoredBook(
            book_id = book_id,
            bookshelf_id = bookshelf_id,
            start_date = body_data.get("start_date"),
            end_date = body_data.get("end_date")
        )
        # add book to the bookshelf
        db.session.add(storedBook)
        db.session.commit()
        return {"message": f"Book {book_id} added succesfully to bookshelf {bookshelf_id}!"}
    # else
    else:
        #return error message
        return {"error": f"Book {book_id} coudln't be added to bookshelf {bookshelf_id}"}, 404
