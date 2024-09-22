from datetime import date, datetime

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.book_comments import BookComment, book_comment_schema, book_comments_schema
from models.books import Book

# creation of book_comments blueprint
book_comments_bp = Blueprint("book_comments", __name__, url_prefix="/<int:book_id>/book_comments")

# create a book_comment route
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
        date = date.today(),
        book = book,
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

# /books/<int:book_id>/book_comments/<int:book_comment_id - DELETE - delete a book_comment
@book_comments_bp.route("/<int:book_comment_id>", methods=["DELETE"])
@jwt_required()
def delete_book_comment(books_id, book_comment_id):
    # fetch the book_comment from books_shelves with id=comment_id
    stmt = db.select(BookComment).filter_by(book_comment_id)
    book_comment = db.session.scalar(stmt)
    # if book_comment exists
    if book_comment:
        # delete the book_comment
        db.session.delete(book_comment)
        db.session.commit()
        # return acknowledgement message
        return {"message": f"Book_comment {book_comment.comment} deleted successfully!"}
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
    stmt = db.select(BookComment).filter_by(id=book_comment_id)
    book_comment = db.session.scalar(stmt)
    # if the book_comment exists
    if book_comment:
        # update book_comment
        # parsing 'date'
        book_comment.date = body_data.get("date") or book_comment.date
        if date:
            try:
                book_comment.date = datetime.strptime(date, '%Y-%m-%d').date()
            except ValueError:
                return {"error": "Expected format for publication_date is YYYY-MM-DD"}, 400
            
        book_comment.comment = body_data.get("comment") or book_comment.comment

        # commit to books_shelves
        db.session.commit()
        
        # return acknowledgement 
        return book_comment_schema.dump(book_comment)
    # else
    else:
        # return an error message
        return {"error": f"Book_comment with id {book_comment_id} not found"}, 404