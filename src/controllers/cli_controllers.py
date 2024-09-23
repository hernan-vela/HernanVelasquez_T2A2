from datetime import date

from flask import Blueprint
from init import db, bcrypt
from models.users_profiles import User
from models.bookshelves import Bookshelf
from models.book_comments import BookComment
from models.stored_books import StoredBook
from models.books import Book

db_commands = Blueprint("db", __name__)

# command to create the table
@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created!")

# command to populate the table
@db_commands.cli.command("seed")
def seed_tables():
    users = [
        User(
            name = "Hernan Vela",
            email = "hernan_admin@email.com",
            user_name = "hernan-vela",
            password = bcrypt.generate_password_hash("3436336").decode("utf-8"),
            is_admin = True
        ),
        User(
            name = "Vittoria Vetra",
            email = "vittoria.vetra@email.com",
            user_name = "vittoria.vetra",
            password = bcrypt.generate_password_hash("vv3436336").decode("utf-8")
        )
    ]

    db.session.add_all(users)

    bookshelves = [
        Bookshelf(
            status = "reading",
            start_date = date.today(),
            review = "I haven't finished it, but it is a must-to-read book",
            user = users[0]
        ), 
        Bookshelf(
            status = "reading",
            start_date = date.today(),
            review = "Intense",
            user = users[0]            
        )
    ]

    db.session.add_all(bookshelves)

    books = [
        Book(
            title = "The Indispensable Calvin and Hobbes: A Calvin and Hobbes Treasury",
            author = "Bill Watterson",
            language = "English",
            translator = "Ed Mont",
            publisher = "Scholastic",
            publisher_city = "New York",
            publication_date = "1992-03-03",
            ebook_isbn = "9780590471794",
            print_isbn = "9880590471794"
        ), 
        Book(
            title = "Autobiography of a Yogi",
            author = "Paramahansa Yogananda",
            language = "English",
            translator = "",
            publisher = "Crystal Clarity Publishers",
            publisher_city = "Chicago",
            publication_date = "1946-05-05",
            ebook_isbn = "9380590471004",
            print_isbn = "9781565892125"
        )
    ]

    db.session.add_all(books)
# IS IT RIGHT? WHAT ABOUT book_id?
    book_comments = [
        BookComment(
            date = date.today(),
            user = users[1],
            book = books[0],
            comment = "Incredible story. I couldn't recommend it more" 
        ), 
        BookComment(
            date = date.today(),
            user = users[0],
            book = books[0],
            comment = "It was a good read for my 4 hours flight."    
        )
    ]

    db.session.add_all(book_comments)

    db.session.commit()

    print("Tables seeded!")

# command to drop the table
@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped.")

 