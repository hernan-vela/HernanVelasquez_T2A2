from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.book_comments import BookComment, book_comment_schema, book_comments_schema
from models.books import Book

# creation of book_comments blueprint
book_comments_bp = Blueprint("book_comments", __name__, url_prefix="/<int:book_id>/book_comments")
# SHOULD I REGISTER 'book_comments_bp' IN 'books_controller.py' SUCH AS IN THE TRELLO EXAMPLE FOR cards_controller?

# /book_id/book_comments - GET - fetch all book_comments
@book_comments_bp.route("/")
def get_all_book_comments():
    stmt = db.select(BookComment)
    book_comments = db.session.scalars(stmt)
    return book_comments_schema.dump(book_comments)

# /book_comment/<id> - GET - fetch a specific book_comment
@book_comments_bp.route("/<int:book_comment_id>")
def get_a_book_comment(book_comment_id):
    stmt = db.select(BookComment).filter_by(id=book_comment_id)
    book_comment = db.session.scalar(stmt)
    if book_comment:
        return book_comment_schema.dump(book_comment)
    else:
        return {"error": f"The book_comment with id {book_comment_id} does not exist"}, 404

# /book_comment - POST - create a new book_comment
@book_comments_bp.route("/", methods=["POST"])
@jwt_required()
def create_book_comment(book_id):
    # get the data from the body of the request
    body_data = request.get_json()
    # fetch the book with id=book_id
    stmt = db.select(Book).filter_by(id=book_id)
    book = db.session.scalar(stmt)
    # if book exists:
    if book:
        # create a new book_comment model instance
        book_comment = BookComment(
        date = date.today("date"),
        book = book
        comment = body_data.get("comment"),  
        user_id = get_jwt_identity()  
        )
        # add and commit to book_comments
        db.session.add(book_comment)
        db.session.commit()
        # response message
        return book_comment_schema.dump(book_comment), 201
    # else 
    else:
        # return error
        return {"error": f"Book with id {book_id} not found"}, 404

# /book_comment/<id> - DELETE - delete a book_comment
@book_comments_bp.route("/<int:book_comment_id>", methods=["DELETE"])
@jwt_required()
def delete_book_comment(book_comment_id):
    # fetch the book_comment from books_shelves
    stmt = db.select(BookComment).filter_by(book_comment_id)
    book_comment = db.session.scalar(stmt)
    # if book_comment exists
    if book_comment:
        # delete the book_comment
        db.session.delete(book_comment)
        db.session.commit()
        # return acknowledgement message
        return {"message": f"Book_comment {book_comment.book_comment_id} deleted successfully!"}
    # else
    else:
        # return error message
        return {"error": f"Book_comment with id {book_comment_id} does not exist"}, 404

# /book_comment/<id> - PUT, PATCH - edit a book_comment entry
@book_comments_bp.route("/<int:book_comment_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_book_comment(book_comment_id):
    # get the info from the body of the request
    body_data = request.get_json()
    # get the book_comment from books_shelves
    stmt = db.select(BookComment).filter_by(id=book_comment_id)
    book_comment = db.session.scalar(stmt)
    # if the book_comment exists
    if book_comment:
        # update the field as required
        # IS THIS THE ONLY ATTRIBUTE THAT CAN BE MODIFIED? OTHERS ARE 'id'
        book_comment.date = body_data.get(date) or book_comment.date
        book_comment.comment = body_data.get("comment") or book_comment.comment
        # commit to books_shelves
        db.session.commit()
        # return acknowledgement 
        return book_comment_schema.dump(book_comment)
    # else
    else:
        # return an error message
        return {"error": f"Book_comment with id {book_comment_id} not found"}, 404