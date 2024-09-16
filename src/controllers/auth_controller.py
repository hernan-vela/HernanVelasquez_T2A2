from flask import Blueprint, request
from models.user import User, user_schema
from init import bcrypt, db
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# route to user registration
@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        # get the data from the body of the request
        body_data = request.get_json()
        # create an instance of the User Model
        user = User(
            name = body_data.get("name"),
            email = body_data.get("email")
        )
        # hash the password
        password = body_data.get("password")
        if password:
            user.passowrd = bcrypt.generate_password_hash(password).decode("utf-8")
        # add and commit to book_shelves db
        db.session.add(user)
        db.session.commit()
        # return confirmation
        return user_schema.dump(user), 201
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The column {err.orig.diag.column_name} is required"}, 400
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "Email address is required"}, 400


# # route to user login (authentication)
# @auth_bp.route("/login")

