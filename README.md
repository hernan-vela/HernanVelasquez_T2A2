# HernanVelasquez_T2A2

Steps to create code the API:

1. Create a local repository and with ```docs``` and ```src``` folders. Inside ```src``` creaate folders for:
- init.py
- main.py
- .venv
- .env
- .env.sample
- .flaskenv
- .gitignore
- requirements.txt (optional. This will be created when we freeze our first module/package/library/extension)

2. Create database, user, and grant permission for user and schema:
    ```CREATE DATABASE books_shelves;
    CREATE USER hernan_dev WITH PASSWORD '3436336';
    GRANT ALL PRIVILEGES ON DATABASE books_shelves TO hernan_dev;
    \c books_shelves #Connect to the database
    GRANT ALL ON SCHEMA public to hernan_dev;
    ```

3. Create ```models``` folder and store here a model representing each one of the entities: user_profile, books, bookshelf, stored_book, book_comment

4. Create ```controllers``` folder and store here the **commands line interface** (cli) as ```cli_controllers.py```

5. In the ```cli_controllers.py``` we create functions to **create**, **seed** and **drop** tables. At the 'seed' command we create as many instances as we wish (at least two) that illustrate keys in the table, as examples.

6. In the ```auth_controller.py``` we  load the Blueprint for the authorisation feature, register the Blueprint in the ```main.py```, and create routes to **register** and **login** a user. Usually the sequence for the route is: get --> add --> commit --> dump.

