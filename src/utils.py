from flask_jwt_extended import get_jwt_identity

import functools

from init import db
from models.users_profiles import User

# Creating a decorator for authorise_as_admin
def auth_as_admin_decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        # get user_id from get_jwt_identity
        user_id = get_jwt_identity()
        # fetch the user from the db books_shelves
        stmt = db.select(User).filter_by(user_id=user_id)
        user = db.session.scalar(stmt)
        # if user is_admin=True
        if user.is_admin:
            # allow the decorator fn to execute
            return fn(*args, **kwargs)
        # else
        else:
            # return error
            return {"error": "Only admin can perform this action"}, 403
    
    return wrapper
