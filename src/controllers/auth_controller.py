from flask import Blueprint, request

from models.bookshelves import Bookshelf
from models.users_profiles import User, user_schema, users_schema, all_users_schema, UserSchema, AllUserSchema
from init import bcrypt, db
from utils import auth_as_admin_decorator

from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from datetime import date, timedelta

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# user registration
@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        # get the data from the body of the request
        body_data = UserSchema().load(request.get_json())
        # create an instance of the User Model
        user = User(
            name = body_data.get("name"),
            email = body_data.get("email"),
            user_name = body_data.get("user_name"),
            bookshelves = [
                Bookshelf(
                    status = "Read"
                ), 
                Bookshelf(
                    status = "Reading"
                ),
                Bookshelf(
                    status = "To-read"
                )
            ]
        )
        # hash the password
        password = body_data.get("password")
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
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

# user login operation
@auth_bp.route("/login", methods=["POST"])
def login_user():
    # get the data from the body of the request
    body_data = request.get_json()
    # find the user in books_shelves with that email address
    stmt = db.select(User).filter_by(email=body_data.get("email"))
    user = db.session.scalar(stmt)
    # if user exists and password is correct
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # create JWT
        token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))
        # respond back
        return {"email": user.email, "is_admin": user.is_admin, "token": token}
    # else
    else:
        # respond back with an error message
        return {"error": "Email or password incorrect"}, 400
    

# GET - a list of users (only admin)
@auth_bp.route("/users_profiles")
@jwt_required()
# authenticate user as admin
@auth_as_admin_decorator
def get_all_users():

    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return all_users_schema.dump(users)

# /auth/users/user_id
@auth_bp.route("/users_profiles/<int:user_id>", methods=["PUT", "PATCH"])
@jwt_required()
#@auth_as_admin_decorator
def update_user(user_id):
    # get field from the body of the request
    body_data = UserSchema().load(request.get_json(), partial=True)
    password = body_data.get("password")
    # fetch the user from 'books_shelves'
    stmt = db.select(User).filter_by(user_id=user_id)
    user = db.session.scalar(stmt)
    # if exists:
    if user:
        # update fields as required
        user.name = body_data.get("name") or user.name
        user.user_name = body_data.get("user_name") or user.user_name
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
        # commit changes to 'books_shelves'
        db.session.commit()
        # return meaningful message
        return user_schema.dump(user)
    # else:
    else:
        # return an error message
        return {"error": "User does not exist."}

# DELETE - eliminate an user (only admin)
@auth_bp.route("/users_profiles/<int:user_id>", methods=["DELETE"])
@jwt_required()
@auth_as_admin_decorator
def delete_user(user_id):
    # find the user with the id from the db
    stmt = db.select(User).filter_by(user_id=user_id)
    user = db.session.scalar(stmt)
    # if exists:
    if user:
        # delete the user
        db.session.delete(user)
        db.session.commit()
        # return an acknowledgement message
        return {"message": f"User with id {user_id} is deleted."}
    # else:
    else:
        # return error message
        return {"message": f"User with id {user_id} not found."}, 404
    

