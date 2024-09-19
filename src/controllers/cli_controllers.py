from datetime import date

from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.bookshelf import Bookshelf

db_commands = Blueprint("db", __name__)

# command to create the table
@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created!")

# command to populate the table
@db_commands.cli.command("seed")
def seed_tables():
    user_profile = [
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

    db.session.add_all(user_profile)

    bookshelf = [
        Bookshelf(
            title = "1984",
            status = "reading",
            start_date = date.today(),
            review = "I haven't finished it, but it is a must-to-read book",
            user = users[0]
        ), 
        Bookshelf(
            title = "Crime and Punishment",
            status = "reading",
            start_date = date.today(),
            review = "Intense",
            user = users[0]            
        )
    ]

    db.session.add_all(bookshelf)
    
    db.session.commit()

    print("Tables seeded!")

# command to drop the table

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped.")

 