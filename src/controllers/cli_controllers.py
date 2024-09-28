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
            password = bcrypt.generate_password_hash("vv3436336").decode("utf-8"),
            is_admin = False
        ),
        User(
            name = "Quino Qaro",
            email = "quino.qaro@email.com",
            user_name = "quino.qaro",
            password = bcrypt.generate_password_hash("qq3436336").decode("utf-8"),
            is_admin = False
        )
    ]

    db.session.add_all(users)

    bookshelves = [
        Bookshelf(
            status = "read",
            user = users[0]
        ), 
        Bookshelf(
            status = "reading",
            user = users[0]            
        ),
        Bookshelf(
            status = "to-read",
            user = users[0]
        ), 
        Bookshelf(
            status = "read",
            user = users[1]            
        ),
        Bookshelf(
            status = "reading",
            user = users[1]
        ), 
        Bookshelf(
            status = "to-read",
            user = users[1]            
        ),
        Bookshelf(
            status = "read",
            user = users[2]
        ), 
        Bookshelf(
            status = "reading",
            user = users[2]            
        ),
        Bookshelf(
            status = "to-read",
            user = users[2]
        )
    ]

    db.session.add_all(bookshelves)

    books = [
        Book(
            title = "Requiem for a nun",
            author = "William Faulkner",
            language = "English",
            translator = "",
            publisher = "Random House",
            publisher_city = "United Kingdom",
            publication_date = "2013-07-05",
            ebook_isbn = "9781446485651",
            print_isbn = "7780590471777"
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
        ),
        Book(
            title = "Flatland",
            author = "Scott Atkins",
            language = "English",
            translator = "",
            publisher = "Geometry",
            publisher_city = "Chicago",
            publication_date = "1955-01-01",
            ebook_isbn = "2280590471004",
            print_isbn = "2281565892125"
        ),
        Book(
            title = "Life of Pi",
            author = "Yann Martel",
            language = "English",
            translator = "Regit Tanger",
            publisher = "Blomsbury",
            publisher_city = "Toronto",
            publication_date = "2022-01-27",
            ebook_isbn = "9781350295698",
            print_isbn = "3381565892145"
        )
    ]

    db.session.add_all(books)

    book_comments = [
        BookComment(
            date = date.today(),
            user = users[0],
            book = books[0],
            comment = "Good Story" 
        ), 
        BookComment(
            date = date.today(),
            user = users[1],
            book = books[0],
            comment = "Marvelous"    
        ),
        BookComment(
            date = date.today(),
            user = users[2],
            book = books[0],
            comment = "No good." 
        ), 
        BookComment(
            date = date.today(),
            user = users[2],
            book = books[0],
            comment = "I re-read. I relate now."   
        ),
        BookComment(
            date = date.today(),
            user = users[2],
            book = books[1],
            comment = "Enlightening" 
        ), 
        BookComment(
            date = date.today(),
            user = users[2],
            book = books[2],
            comment = "Better than the movie."   
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

 