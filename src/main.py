import os
from flask import Flask

from init import db, ma, bcrypt, jwt
from controllers.cli_controllers import db_commands
from controllers.auth_controller import auth_bp
from controllers.bookshelves_controller import bookshelves_bp
from controllers.book_comments_controller import book_comments_bp
from controllers.books_controller import books_bp
from controllers.stored_books_controller import stored_books_bp

def create_app():
    app = Flask(__name__)
    # makes order of entries determined by schemas
    app.json.sort_keys = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(db_commands)
    app.register_blueprint(auth_bp)
    app.register_blueprint(bookshelves_bp)
    app.register_blueprint(book_comments_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(stored_books_bp)

    return app