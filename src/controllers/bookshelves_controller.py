from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.bookshelves import Bookshelf, bookshelf_schema, bookshelves_schema


bookshelves_bp = Blueprint("bookshelf", __name__, url_prefix="/bookshelf")

# /bookshelf - GET - fetch all bookshelves of a user
# @bookshelves_bp.route("/")
# def get_all_bookshelves():
#     stmt = db.select(Bookshelf)
#     bookshelves = db.session.scalars(stmt)
#     return bookshelves_schema.dump(bookshelves)

# GET A BOOKSHELF FROM AN SPECIFIC USER  
# /<int:user_id>/bookshelf/<int:bookshelf_id>
#      /bookshelf/<id> - GET - fetch a specific bookshelf
@bookshelves_bp.route("/")
@jwt_required()
def get_a_bookshelf(bookshelf_id):
    user_id = get_jwt_identity()
    stmt = db.select(Bookshelf).filter_by(user_id=user_id)
    bookshelf = db.session.scalar(stmt)
    if bookshelf:
        return bookshelf_schema.dump(bookshelf)
    else:
        return {"error": f"Bookshelf with id {bookshelf_id} does not exist"}, 404

# adding a book to a bookshelf
#/<int:user_id>/bookshelf/<int:bookshelf_id>/<int:book_id>
#               /bookshelf - POST - create a new book in bookshelf
@bookshelves_bp.route("/", methods=["POST"])
@jwt_required()
def create_bookshelf():
    # get the data from the body of the request
    body_data = bookshelf_schema.load(request.get_json())
    # create a new bookshelf model instance
    bookshelf = Bookshelf(
        status = body_data.get("status"),
        start_date = body_data.get("start_date"),
        end_date = body_data.get("end_date"),
        review = body_data.get("review"),
        user_id = get_jwt_identity()
    )
    # add and commit to bookshelves
    db.session.add(bookshelf)
    db.session.commit()
    # response message
    return bookshelf_schema.dump(bookshelf)

# /bookshelf/<id> - DELETE - delete a bookshelf
@bookshelves_bp.route("/<int:bookshelf_id>", methods=["DELETE"])
@jwt_required()
def delete_bookshelf(bookshelf_id):
    # fetch the bookshelf from the database
    stmt = db.select(Bookshelf).filter_by(id=bookshelf_id)
    bookshelf = db.session.scalar(stmt)
    # if bookshelf exists
    if bookshelf:
        # delete the bookshelf
        db.session.delete(bookshelf)
        db.session.commit()
        return {"message": f"Bookshelf {bookshelf.title} deleted succesfully!"}
    # else
    else:
        #return error message
        return {"error": f"Bookshelf with id {bookshelf_id} does not exist"}, 404

# /bookshelf/<id> - PUT, PATCH - edit a bookshelf entry
@bookshelves_bp.route("/<int:bookshelf_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_bookshelf(bookshelf_id):
    # get the info from the body of the request
    body_data = bookshelf_schema.load(request.get_json())
    # get the bookshelf from the bookshelves
    stmt = db.select(Bookshelf).filter_by(id=bookshelf_id)
    bookshelf = db.session.scalar(stmt)
    # if the bookshelf exists
    if bookshelf:
        # if the user is not the bookshelf owner
        if str(bookshelf.user_id) != get_jwt_identity():
            # return error message
            return {"error": "Only the owner of the bookshelf is allowed to perform this operation"}

        # update the fields as required
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