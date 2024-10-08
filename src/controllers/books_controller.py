from datetime import datetime
 
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.books import Book, book_schema, books_library_schema

from controllers.book_comments_controller import book_comments_bp

from utils import auth_as_admin_decorator

books_bp = Blueprint("books", __name__, url_prefix="/books")
books_bp.register_blueprint(book_comments_bp)

# /books - GET - fetch all books
@books_bp.route("/")
def get_all_books():
    stmt = db.select(Book)
    books = db.session.scalars(stmt)
    return books_library_schema.dump(books)

# /books/<id> - GET - fetch a specific book
@books_bp.route("/<int:book_id>")
def get_a_book(book_id):

    # filter the entity 'books' by book_id
    stmt = db.select(Book).filter_by(book_id=book_id)
    book = db.session.scalar(stmt)
    if book :
        return book_schema.dump(book)
    else:
        return {"error": f"Book with id {book_id} does not exist"}, 404
    
# /books - POST - create a new book
@books_bp.route("/", methods=["POST"])
@jwt_required()
@auth_as_admin_decorator
def create_book():
    # get the data from the body of the request
    body_data = book_schema.load(request.get_json())

    publication_date = body_data.get("publication_date")
    
    # parsing the publication date
    if publication_date:
        try:
            publication_date = datetime.strptime(publication_date, '%Y-%m-%d').date()
        except ValueError:
            return {"error": "Expected format for publication_date is YYYY-MM-DD"}, 400
    else:
        publication_date = None

    # create a new book model instance        
    book = Book(
        title = body_data.get("title"),
        author = body_data.get("author"),
        language = body_data.get("language"),
        translator = body_data.get("translator"),
        publisher = body_data.get("publisher"),
        publisher_city = body_data.get("publisher_city"),
        publication_date = publication_date,
        ebook_isbn = body_data.get("ebook_isbn"),
        print_isbn = body_data.get("print_isbn") 
    )
    # add and commit to book
    db.session.add(book)
    db.session.commit()
	# return reponse message
    return book_schema.dump(book)

# /books/<id> - DELETE - delete a book
@books_bp.route("/<int:book_id>", methods=["DELETE"])
@jwt_required()
@auth_as_admin_decorator
def delete_book(book_id):
    # fetch the book from books_shelves
    stmt = db.select(Book).filter_by(book_id=book_id)
    book = db.session.scalar(stmt)
    # if book exists
    if book:
        # delete the book
        db.session.delete(book)
        db.session.commit()
        return {"message": f"Book {book.book_id} deleted successfully!"}
    # else
    else:
        # return error message
        return {"error": f"Book with id {book_id} does not exist"}, 404

# /books/<id> - PUT, PATCH - edit a book entry
@books_bp.route("/<int:book_id>", methods=["PUT", "PATCH"])
@jwt_required()
@auth_as_admin_decorator
def update_book(book_id):
    # get value from the body of the request
    body_data = book_schema.load(request.get_json(), partial=True)
    # get the book from books_shelves
    stmt = db.select(Book).filter_by(book_id=book_id)
    book = db.session.scalar(stmt)
    
    publication_date = body_data.get("publication_date")
    
    # parsing the publication date
    if publication_date:
        try:
            publication_date = datetime.strptime(publication_date, '%Y-%m-%d').date()
        except ValueError:
            return {"error": "Expected format for publication_date is YYYY-MM-DD"}, 400
    else:
        publication_date = None
    
    if book:
        # update the field as required
        book.title = body_data.get("title") or book.title,
        book.author = body_data.get("author") or book.author
        book.language = body_data.get("language") or book.language
        book.translator = body_data.get("translator") or book.translator
        book.publisher = body_data.get("publisher") or book.publisher
        book.publisher_city = body_data.get("publisher_city") or book.publisher_city
        publication_date = publication_date or book.publication_date
        book.ebook_isbn = body_data.get("ebook_isbn") or book.ebook_isbn
        book.print_isbn = body_data.get("print_isbn") or book.print_isbn

        # commit to books_shelves
        db.session.commit()

        # return acknowledgement message
        return book_schema.dump(book)
    # else
    else:
        # return an error message   
        return {"error": f"Book with id {book_id} not found"}, 404
