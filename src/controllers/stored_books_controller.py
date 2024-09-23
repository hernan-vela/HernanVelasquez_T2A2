# # THIS CONTROLLER CAN PROBABLY BE SUPPRESSED
# # ASK AAMOD AND/OR LUIS

# from datetime import date

# from flask import Blueprint, request
# from flask_jwt_extended import jwt_required, get_jwt_identity

# from init import db
# from models.stored_books import StoredBook, stored_book_schema, stored_books_schema

# stored_books_bp = Blueprint("stored_book", __name__, url_prefix="/<int:bookshelf_id>/<int:book_id/stored_book")

# # DOES THIS OPERATION MAKE SENSE? WILL THIS GIVE ME ALL THE BOOKSHELVES OF ALL THE USERS IN THE SYSTEM?
# # /stored_book - GET - fetch all stored_book
# @stored_books_bp.route("/")
# def get_all_stored_books():
#     stmt = db.select(StoredBook)
#     stored_books = db.session.scalars(stmt)
#     return stored_books_schema.dump(stored_books)
# # /stored_book/<id> - GET - fetch a specific stored_book
# @stored_books_bp.route("/<int:stored_book_id>")
# def get_a_stored_book(stored_book_id):
#     stmt = db.select(StoredBook).filter_by(id=stored_book_id)
#     stored_book = db.session.scalar(stmt)
#     if stored_book:
#         return stored_book_schema.dump(stored_book)
#     else:
#         return {"error": f"Stored_book with id {stored_book_id} does not exist"}, 404



