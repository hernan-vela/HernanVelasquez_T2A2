from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.books import Book
from models.bookshelves import Bookshelf, bookshelf_user_schema, bookshelves_user_schema
from models.stored_books import StoredBook
from models.users_profiles import User

users_profiles_bp = Blueprint("users_profiles", __name__, url_prefix="")

# GET - fetch all the bookshelves of a user
@users_profiles_bp.route("/users_profiles/<int:user_id>/bookshelves")
@jwt_required()
def get_bookshelves(user_id):
    user_id = get_jwt_identity()
    stmt = db.select(Bookshelf).filter_by(user_id=user_id)
    bookshelves = db.session.scalars(stmt)
    if bookshelves:
        return bookshelves_user_schema.dump(bookshelves)
    else:
        return {"error": f"Bookshelves of user {user_id} cannot be found or user does not exist"}, 404