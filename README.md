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

3. Create ```models``` folder and store here a model representing each one of the entities: UserProfile, Books, Bookshelf, StoredBook, BookComment