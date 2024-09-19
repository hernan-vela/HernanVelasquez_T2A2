from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.bookshelf import Bookshelf, bookshelf_schema, bookshelves_schema


bookshelf_bp = Blueprint("bookshelf", __name__, url_prefix="/bookshelf")

# /bookshelf - GET - fetch all bookshelves
@bookshelf_bp.route("/")
def get_all_bookshelves():
    stmt = db.select(Bookshelf)
    bookshelves = db.session.scalars(stmt)
    return bookshelves_schema.dump(bookshelves)

# /bookshelf/<id> - GET - fetch a specific bookshelf
@bookshelf_bp.route("/<int:bookshelf_id>")
def get_a_bookshelf(bookshelf_id):
    stmt = db.select(Bookshelf).filter_by(id=bookshelf_id)
    bookshelf = db.session.scalar(stmt)
    if bookshelf:
        return bookshelf_schema.dump(bookshelf)
    else:
        return {"error": f"Bookshelf with id {bookshelf_id} does not exist"}, 404

# /bookshelf - POST - create a new bookshelf
@bookshelf_bp.route("/", methods=["POST"])
@jwt_required
def create_bookshelf():
    # get the data from the body of the request
    body_data = request.get_json()
    # create a new bookshelf model instance
    bookshelf = Bookshelf(
        title = body_data.get("title"),
        status = body_data.get("status"),
        start_date = body_data.get("start_date"),
        end_date = body_data.get("end_date"),
        review = body_data.get("review"),
        user_id = get_jwt_identity()
    )
    # add and commit to book_shelves
    db.session.add(bookshelf)
    db.session.commit()
    # response message
    return bookshelf_schema.dump(bookshelf)

# /bookshelf/<id> - DELETE - delete a bookshelf
@bookshelf_bp.route("/<int:bookshelf_id", methods=["DELETE"])
@jwt_required
def delete_bookshelf(bookshelf_id):
    # fetch the bookshelf from the database
    stmt = db.select(Bookshelf).filter_by(id=bookshelf_id)
    bookshelf = db.session.scalar(stmt)
    # if bookshelf exists
    if card:
        # delete the bookshelf
        db.session.delete(bookshelf)
        db.session.commit()
        return {"message": f"Bookshelf {bookshelf.title} deleted succesfully!"}
    # else
    else:
        #return error message
        return {"error": f"Bookshelf with id {bookshelf_id} does not exist"}, 404

# /bookshelf/<id> - PUT, PATCH - edit a bookshelf entry
@bookshelf_bp.route("/<int:bookshelf_id", methods=["PUT", "PATCH"])
@jwt_required
def update_bookshelf(bookshelf_id):
    # get the info from the body of the request
    body_data = request.get_json()
    # get the bookshelf from the books_shelves
    stmt = db.select(Bookshelf).filter_by(id=bookshelf_id)
    bookshelf = db.session.scalar(stmt)
    # if the bookshelf exists
    if bookshelf:
        # update the fields as required
        bookshelf.title = body_data.get("title") or bookshelf.title
        bookshelf.status = body_data.get("status") or bookshelf.status
        bookshelf.start_date = body_data.get("start_date") or bookshelf.start_date
        bookshelf.end_date = body_data.get("end_date") or bookshelf.end_date
        bookshelf.review = body_data.get("review") or bookshelf.review
        # commit to books_shelves
        db.session.commit()
        # return acknowledgement message
        return bookshelf_schema.dump(bookshelf)
    # else
    else:
        # return an error message
        return {"error": f"Bookshelf with id {bookshelf_id} not found"}, 404