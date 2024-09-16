from flask import Blueprint
from init import db, bcrypt
from models.user import User

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
            password = bcrypt.generate_password_hash("3436336").decode("utf-8")
        )
    ]

    db.session.add_all(user_profile)

    db.session.commit()

    print("Tables seeded!")

# command to drop the table

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped.")

 