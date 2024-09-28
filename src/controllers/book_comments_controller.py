from datetime import date, datetime

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.book_comments import BookComment, book_comment_schema, book_comments_schema 
from models.books import Book

# creation of book_comments blueprint
book_comments_bp = Blueprint("book_comments", __name__, url_prefix="/books/<int:book_id>/book_comments")


# /book_comment - POST - create a new book_comment
@book_comments_bp.route("/", methods=["POST"])
@jwt_required()
def create_book_comment(book_id):
    # get the data from the body of the request
    body_data = book_comment_schema.load(request.get_json())

    # fetch the book with id=book_id
    stmt = db.select(Book).filter_by(book_id=book_id)
    book = db.session.scalar(stmt)

    # if book exists:
    if book:
        # create a new book_comment model instance
        book_comment = BookComment(
        user_id = get_jwt_identity(),
        date = date.today(),
        book = book,
        comment = body_data.get("comment") 
        )

        # add and commit to book_comments
        db.session.add(book_comment)
        db.session.commit()

        # response message
        return book_comment_schema.dump(book_comment), 201
    else:
        # return error
        return {"error": f"Book with id {book_id} not found"}, 404




# DELETE - delete a book_comment
@book_comments_bp.route("/<int:book_comment_id>", methods=["DELETE"])
@jwt_required()
def delete_book_comment(book_comment_id):

    # check if the authenticated user owns the book_comment
    user = get_jwt_identity()

    # fetch the book_comment to check existence and ownership
    stmt = db.select(BookComment).filter_by(user_id=user, book_comment_id=book_comment_id)
    book_comment = db.session.scalar(stmt)

    # nice message if not existence, or ownership
    if not book_comment:
        return {"message": "Book comment not found or not owned by the user."}, 404

    # fetch the book_comment from books_shelves with id=comment_id
    stmt = db.select(BookComment).filter_by(book_comment_id=book_comment_id)
    book_comment = db.session.scalar(stmt)
    # if book_comment exists
    if book_comment:
        # delete the book_comment
        db.session.delete(book_comment)
        db.session.commit()
        # return acknowledgement message
        return {"message": f"Book_comment {book_comment_id} deleted successfully!"}
    # else
    else:
        # return error message
        return {"error": f"Book_comment with id {book_comment_id} does not exist"}, 404








# /books/book_id/book_comments/book_comment_id- PUT, PATCH - edit a book_comment entry
@book_comments_bp.route("/<int:book_comment_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_book_comment(book_id, book_comment_id):
    # get the info from the body of the request
    body_data = request.get_json()
    # get the book_comment from books_shelves
    stmt = db.select(BookComment).filter_by(book_comment_id=book_comment_id)
    book_comment = db.session.scalar(stmt)
    # if the book_comment exists
    if book_comment:
        # update book_comment        
        book_comment.comment = body_data.get("comment") or book_comment.comment
        # commit to books_shelves
        db.session.commit()

        # return acknowledgement 
        return book_comment_schema.dump(book_comment)
    # else
    else:
        # return an error message
        return {"error": f"Book_comment with id {book_comment_id} not found"}, 404