from flask import Blueprint, request
from models.user import User, user_schema
from init import bcrypt, db
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token
from datetime import timedelta

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


@auth_bp.route("/login", methods=["POST"])
def login_user():
    # get the data from the body of the request
    body_data = request.get_json()
    # find the user in books_shelves with that email address
    stmt = db.select(User).filter_by(email=body_data["email"])
    user = db.session.scalar(stmt)
    # If user exists and password is correct
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # create JWT
        token = create_access_token(identity=str(user.id), expire_delta=timedelta(days=1))
        # respond back
        return {"email": user.email, "is_admin": user.is_admin, "token": token}
    # else
    else:
        # respond back with an error message
        return {"error": "Email of password incorrect"}, 400


