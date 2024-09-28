from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.bookshelves import Bookshelf, bookshelves_user_schema
from models.users_profiles import User

users_profiles_bp = Blueprint("users_profiles", __name__, url_prefix="/users_profiles")

# GET - fetch all the bookshelves and books of a user
@users_profiles_bp.route("/<int:user_id>/bookshelves")
@jwt_required()
def get_bookshelves(user_id):

    # check if user querying is registered
    user = db.session.get(User, user_id)
    if not user:

        # return message if the user requested does not exist in the database
        return {"error": f"User with id {user_id} does not exist"}, 404
    
    # checks existence and ownership of bookshelves
    stmt = db.select(Bookshelf).filter_by(user_id=user_id)
    bookshelves = db.session.scalars(stmt)
    if bookshelves:
        return bookshelves_user_schema.dump(bookshelves)
    else:
        return {"error": f"Bookshelves of user {user_id} cannot be found or user does not exist"}, 404
