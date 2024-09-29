# Coder Academy Full Stack Web Development Diploma
## HernanVelasquez_T2A2 
## API Server


### Allocation and tracking of tasks throughout the API project

Considering the timeframe, and workload for my skills and priorities, the project was planned with 5 main stages, as follows: draft models, draft controllers, complete CRUD operations for app features, test endopoints and debugging until endpoints work flawlessly. The layout of the project plan can be witnessed in **Trello** where the cards show deadlines, and additional checklists to detail each stage.

#### Trello: [Books & Shelves management resource](https://trello.com/invite/b/66e391591a3af71aa21050d1/ATTI9da0294d53b14ef5deb7617a03729a38213C333E/api-server-t2a2)
(Please, access **Trello** as a member to view this content)


![day-0](./docs/trello-screenshots/Screenshot%202024-09-22%20at%2010.33.39 PM.png)
Day 0 of the API project.

#### Stage 0. Create local & remote repo in Github
**Deadline: Sep 23, 2024 / 22:00**

![stage-0](./docs/trello-screenshots/Screenshot%202024-09-23%20at%201.44.33 PM.png)
Creation of repository and main folders

![stage-0](./docs/trello-screenshots/Screenshot%202024-09-23%20at%203.32.26 PM.png)
Completion of repository skeleton

#### Stage 1. Drafting models for each entity
**Deadline: Sep 23, 2024 / 22:00**

![draft-models](./docs/trello-screenshots/Screenshot%202024-09-23%20at%203.46.57 PM.png)
Models of entities

![users_profiles-model](./docs/trello-screenshots/Screenshot%202024-09-23%20at%203.47.30 PM.png)
Completion of 'users_profiles' model

![bookshelves-book_comments-models](./docs/trello-screenshots/Screenshot%202024-09-23%20at%205.38.00 PM.png)
Completion of 'bookshelves' and 'book_comments' models

![models-completed](./docs/trello-screenshots/Screenshot%202024-09-23%20at%206.36.07 PM.png)
Drafting models: completed

#### Stage 2. Drafting controllers for relevant operations
**Deadline: 25 Sep, 2024 / 22:00**

![drafting-controllers](./docs/trello-screenshots/Screenshot%202024-09-24%20at%204.40.09 PM.png)
Completion of cli, book_comments, books and auth controllers

At this stage was clear that given that the entity ```stored_books``` is a junction entity, CRUD operations are not relevant here for this specific project.

![controllers-complete](./docs/trello-screenshots/Screenshot%202024-09-24%20at%207.25.35 PM.png)
Completion of controllers drafts

#### Stage 3. Complete authorisation for relevant CRUD operations
**Deadline: 26 Sep, 2024 / 22:00**

![crud-operations](./docs/trello-screenshots/Screenshot%202024-09-24%20at%205.25.25 PM.png)
CRUD operations planned for the API (early stage)

![c-book-d-book](./docs/trello-screenshots/Screenshot%202024-09-25%20at%205.09.43 PM.png)
Operations of adding and creating a book

![crud-updated](./docs/trello-screenshots/Screenshot%202024-09-25%20at%208.31.19 PM.png)
More CRUD operations added. Fetching all books and a specific book, complete (midterm stage)

![crud-get-comments](./docs/trello-screenshots/Screenshot%202024-09-25%20at%209.13.37 PM.png)
More CRUD operations added. Creat a book comment, get comments per book, and per user complete

![all-crud-but-bookshelves](./docs/trello-screenshots/Screenshot%202024-09-26%20at%204.31.41 PM.png)
Most of CRUD operations completed, except CRU for bookshelves

![crud-complete](./docs/trello-screenshots/Screenshot%202024-09-26%20at%206.34.09 PM.png)
CRUD complete. Afterwards, during the testing period the operation to update a bookshelf, more precisely a stored book in a bookshelf, was dismissed to mantain the simplicity of the API.

#### Stages 4 & 5. Testing endpoints / Debugging
**Deadline: 26 Sep, 2024 / 22:00**

These tasks are performed simultaneously, before the last and final testing.

![testing-endpoints](./docs/trello-screenshots/Screenshot%202024-09-25%20at%209.14.21 PM.png)
Beginning of tests for each endopoints. Here, the most of endpoints should run without crashing.

![endpoints](./docs/trello-screenshots/Screenshot%202024-09-25%20at%209.14.37 PM.png)
Endpoints register and login completed

![endpoints](./docs/trello-screenshots/Screenshot%202024-09-26%20at%209.46.09 PM.png)
Completion of CRUD operation endpoints for users, books and book comments. 

![endpoints-completed](./docs/trello-screenshots/Screenshot%202024-09-26%20at%2010.39.12 PM.png)
Endpoints working well. Small adjustments in the final stage of debugging. Updating a stored book in a bookshelf was discarded.

#### Final Stage. Final test of endpoints
**Deadline: 27 Sep, 2024 / 22:00**

![final-test-endpoints](./docs/trello-screenshots/Screenshot%202024-09-29%20at%203.01.24 AM.png)
Final test for the endpoints completed

#### Overview of the evolution of the API project

![repo-models](./docs/trello-screenshots/Screenshot%202024-09-23%20at%203.33.02 PM.png)
Repo created and working on drafting models

![controllers](./docs/trello-screenshots/Screenshot%202024-09-23%20at%206.37.21 PM.png)
Models completed and working on drafting controllers

![crud-operations](./docs/trello-screenshots/Screenshot%202024-09-24%20at%207.26.05 PM.png)
Controllers finishes. Working on CRUD operations

![testing-endpoints](./docs/trello-screenshots/Screenshot%202024-09-25%20at%209.14.53 PM.png)
Testing endpoints while creating them

![crud-finished-testing-ongoing](./docs/trello-screenshots/Screenshot%202024-09-26%20at%206.34.29 PM.png)
Rough version of CRUD operation finished. Just testing endopoints

![testin-done-debuggin-now](./docs/trello-screenshots/Screenshot%202024-09-26%20at%2010.39.49 PM.png)
Testing completed. Working on debugging. Task overdue

![debugging-and-final-testing](./docs/trello-screenshots/Screenshot%202024-09-27%20at%201.21.44 PM.png)
Debugging and final testing of endopints.

![debugging-and-final-testing-done](./docs/trello-screenshots/Screenshot%202024-09-27%20at%204.41.42 PM.png)
Completion of debugging and final testing of endpoints

![coding-completed](./docs/trello-screenshots/Screenshot%202024-09-27%20at%204.42.13 PM.png)
Coding completed. Next task is documentation.

![documentation-ongoing](./docs/trello-screenshots/Screenshot%202024-09-27%20at%204.42.32 PM.png)
Working on documentation

![project-finished](./docs/trello-screenshots/Screenshot%202024-09-29%20at%203.02.09 AM.png)
Project finished

### Third-Party, Packages and Dependencies used in the API

- **Flask**: web framework that gathers Python modules to develop an API project with less complications, reducing the level of detail, and errors created (Python Basics, 2021)[^flask]

- **os**: module in Python that helps to interact with the **o**perating **s**ystem, at performing standarised tasks such as creating, opening and removing files, among others (GeeksforGeeks, 2024)[^os]. In this project, 'os' is used to interact/access environment variables, such as the database url and the jwt token.

- **Marshmallow**: ORM that provide a group of schemas to validate input, serialise and deserialise information that is exchanged between the front and back end (Marshmallow, 2024)[^marshmallow]

- **fields** from Marshmallow: unpacks information of entities to establish relationships. For example, in this project it allows to take attributes of an entity, filter them and create a more meaningful response for the user. (Marshmallow, 2024)[^m.fields]

- **bcrypt**: cryptographic algorithm used to mask/secure passwords. Bcrypt hides the characters of the password in an apparently random bundle of characters of fixed-length. This value is stored in the database and cannot be reversed to read the password from the random string (freeCodeCamp, 2024)[^bcrypt].

- **Json Web Token (jwt)**: it uses the structure of Header/Payload/Signature to authenticate users, facilitate and simplify the interaction between client and server. It comprises the type of token used and signing algorithm (Header); claims or statements that determine the registered, public or private nature of the interaction (Payload); and a signature that verifies the message and no one has tampered with it along the route (Signature)(JWT, 2024)[^jwt].

- **jwt_required and get_jwt_identity** from flask: these are authentication tools. When a user has already been logged in, the 'jwt_required' protect routes, avoiding third parties to intersect and tamper with information. And with the 'get_jwt_identity' the identity of the user is checked through a JWT in a protected route (Flask, 2022)[^flask-kwt].

- **SQLAlchemy**: denominated the Python SQL, it helps to access databases using Python commands. All the operations performed from the 'psql' such as, 'SELECT', 'FILTER', 'DELETE', 'CREATE', 'DROP', 'ALTER TABLE', among others, can be implemented by using the Python language to automatised the processes (SQlAlchemy, 2024)[^sqlalchemy]

### Pros and Cons of using PostgreSQL

The main advantage of PostreSQL is this DBMS is free to use and distribute, it can handle large amounts of data, supports formats such as JSON, spatial data, and the open-source nature make it helpful when encountering problems, because there are several blogs and documentation online for troubleshooting (PostgreSQL, 2024)[^psql].

Although, some of the drawbacks of the PostgreSQL: keep records of previous keys (as a momentary back-up), which consumes more memory and computing time. Also, it has a sanitisation process to clean and delete all inactive copies, but sometimes the multi-version storage surpasses the sanitisation process and the database gets overloaded (Andy Pavlo, 2023)[^A.Pavlo]

### Features, purpose and functionalites of ORM used in this app

The Books & Bookshelves API has the standard CRUD operations that are mostly applied throughout all the entities in the database. It employes SQLAlchemy to exchange and communicate information between PostgreSQL and the framework, and it uses Marshmallow to serialise and deserialise information between the front end and the back end.
Here it will be discussed the most illustratives and relevants features of the API:

#### User registration

It takes information from the user, and takin the ```UserSchema``` as reference the infromatio is validated. The password created by the user is hashed with Bcrypt and a new profile created with ```{"user_id", "name", "email", "user_name", "password", "is_admin"}```. In addition, the code automatically creates three bookshelves by default where the user stores the books that they have "read", they are currently "reading", and they plan "to-read".

![user-registration](./docs/code-snipets/user-registration.png)
*Code to create a new user in the database*

#### User login

It requests the email and password fromn the body of request. The code automatically filters the the ```users_profiles``` entity by using the email as reference, and it implements a the JWT functonalities to generate a token with expiry date. This token will allow the user to perform other tasks such as query books, book comments, add books to their bookshelves, modifiy books stored in their shelves, delete their own books, and so on.
If the email and password do not match, the system prompts a message explaining this result.

![user-login](./docs/code-snipets/user-login.png)
*Code to login an existent user*

#### Consulting books from the database

The app offers the function to any user to query the list of all the books in the database and query a specific book with its bibliographical information and all the comments associated with that book made by users of the app.

#### Adding a book to a any of your own bookshelves

Each user can add any book to any of their own three bookshelves, and only their bookshelves. The function ```add_book_to_bookshelf``` identifies the user as a registered user, then confirms the existence and ownership of the bookshelf. Next the function confirms that the book desired actually exists. Finally, the book is added to the respective bookshelf.
If at any point any of these conditions are not met, the user receives a message explaining why the operation cannot be performed.


![add-book-bookshelf](./docs/code-snipets/add-book-bookshelf.png)
*Code to add a book to a owned bookshelf*

#### Posting a comment about any book

The information of the book to comment comes from the URL. The function takes the ```book_id```, verify that the user is registered, and takes the ```"comment"``` from input by the user in the body request. Then, the comment is added to the profile of the book.

#### Amending a comment about a book

The only person that can modify a comment is the one that posted such comment. The function ```update_book_comment``` takes the ```book_id``` and the ```book_comment_id``` to check existence and ownership of the comment. If the information is valid, the user can modify the ```"comment"``` attribute, and only this one. Once the comment is changed, the system returns an acknowledgemente message.
If at any point in this logic, any of the conditions are not met, the user receives a message explaining why the operation could not be performed.

![amend-comment](./docs/code-snipets/amend-comment.png)
*Code to amend a comment*

#### Delete a comment about a book

The function ```delete_book_comment``` takes the information of ```book_id``` and ```book_comment_id``` from the URL. Then it checks existence and ownership of the comment, and if these are true, the comment is deleted.
If at any stage, any of these conditions are not met, the user receives a message explaining why the operation cannot be completed.

![delete-comment](./docs/code-snipets/delete-comment.png)
*Code to delete a comment*



### Initial stage of ERD for the Books & Shelves API


![ERD-v.0](./docs/drawio-screenshots/(v.0)BooksApp-ERD.jpg)

The project was initially conceived with 5 entities: UserProfile, Books, BookComments, Bookshelf and StoredBook with relationships among them as follows:

- **UserProfile** (PK: user_id) -- 1 to Many ---> **Books** (FK: user_id): one user can be linked to several books.

- **UserProfile** (PK: user_id) -- 1 to Many ---> **Bookshelf** (FK: user_id): one user can own more than one bookshelf.

- **UserProfile** (PK: user_id) ---- 1 to many ---> **BookComments** (FK: user_id): one user can create many comments of different books.

- **Books** (PK: book_id) -- 1 to Many ---> **BookComments** (FK: book_id): one book can have several comments.

- **Books** (PK: book_id) -- 1 to Many ---> **StoredBook** (FK: book_id): one book can be stored in several bookshelves, then one book can have more than record in the StoreBook entity.

- **Bookshelf** (PK: bookshelf_id) -- 1 to Many ---> **StoredBook** (FK: bookshelf_id): one entry in the bookshelf can be stored more than once in the StoredBook entity.

The 'StoredBook' entity has been established as a join table to facilitate the relation that would exist between 'Books' and 'Bookshelf', which is a Many-Many relation. With the StoredBook entity the complexity of Many-Many is reduced and become manageble in the database.

### Normalised databe of ERD for the Books & Shelves API

![ERD-normalised](./docs/drawio-screenshots/(v.4)BooksApp.png)

After analysis of the database and its implementation, the database has been arranged with more meaningful names to facilitate the coding process, the entities with the bookshelves and the books stored have been restructured, and the relationship between the user entity and the books entity has been dismissed to make a streamline interaction among all the tables.

- **users_profiles** (PK: user_id) -- 1 to Many ---> **bookshelves** (FK: user_id): one user can be linked to 3 bookshelves with status "Read", "Reading" and "To-read"

- **users_profiles** (PK: user_id) -- 1 to Many ---> **book_comments** (FK: user_id): one user can have several comments on different books.

- **books** (PK: book_id) ---- 1 to many ---> **book_comments** (FK: book_id): one book can have many comments.

- **books** (PK: book_id) -- 1 to Many ---> **stored_books** (FK: book_id): one book can be stored in different entries.

- **bookshelves** (PK: bookshelf_id) -- 1 to Many ---> **stored_books** (FK: bookshelf_id): one entry in the bookshelf can be stored more than once in the stored_books entity.

In addition, the attributes of 'start_date' and 'end_date' have been transferred from 'bookshelves' to 'stored_books' while it makes more sense that a user starts reading and finishes a book on any given date, for a book that is ***stored*** in 'stored_books'. Also, the 'review' attribute from the 'bookshelves' is suppressed while the comments fulfil the purpose of commenting about a book

### Models relationships

- **User Model**: establishes a relation of more than one bookshelf per user, with cascading, in case that a user is deleted from the database, their bookshelves are deleted as well.
It also has a relationship where a user can create many comments on one or more books.

![user-model](./docs/code-snipets/user-model.png)
*Example of User Model relationships*

This model also has to different schema: ```UserSchema``` to return the most meaningful information of an user, includins their book comments, and a ```AllUserSchema``` to displayed all the users when the admin requests them, but in a simplified version with only ```{"user_id}, "name", "email"}```

![user-schemas](./docs/code-snipets/user-schemas.png)
*User Schemas in code*

- **Book Model**: here one book can have many comments what means that many users can comment on different books without overlaps. Also, one book can be stored simultaneously in more than one 'stored_book' entry, this helps with the fact that one user with "read", "reading" and "to-read" bookshelves can stored many books one or more of them at the same time.

![book-model](./docs/code-snipets/book-model.png)
*Example of the Book Model relationships*

Here, we also encounter one ```BookSchema``` to retrieve the information of one single books with all its linked comments, and another schema called ```BookLibrarySchema``` to display all the books in the library, but just the relevant information of ```{"book_id", "title", "author"}```.

![book-schemas](./docs/code-snipets/user-schemas.png)
*Book Schemas in code*

- **BookComment Model**: accordingly to the Book Model, here a user can make several comments, and one book can have many comments.

![book-comment-model](./docs/code-snipets/book-comments-model.png)
*Example of the BookComment Model relationships*

In this case, there is only one BookComment schema what meets all the purposes of the app

![book-comment-schema](./docs/code-snipets/book-comments-schema.png)
*BookComment Schema in code*

- **Bookshelf Model**: there is a relationship where one user can have three bookshelves, "read", "reading" and "to-read". Also, one bookshelf can have many records in the 'stored_books' entity. This model disrupts the complicated relationship between 'books' and 'bookshelves', where many books could be in many bookshelves. With the 'stored_books' join table, the DBMS is more effective.

![bookshelf-model](./docs/code-snipets/bookshelf-model.png)
*Example of the Bookshelf Model relationships*

In this case, one single Bookshelf schema is valid to handle the information, according to the API features.

![bookshelf-schema](./docs//code-snipets/bookshelves-schema.png)
*Bookshelf schema in code*

- **StoredBook Model**: given its nature of join table between 'books' and 'bookshelves', the StoredBook Model is such that one book can be stored in many entries of the 'stored_books' table, and one bookshelf can have several entries in the 'stored_books' table.

![stored-book-model](./docs/code-snipets/stored-book-model.png)
*Example of the StoredBook Model relationships*

Here, with one schema, it is possible the retrieve the information of ```{"stored_book_id", "book_id", "title", "author", "bookshelf_id", "user", "status"}```



### Operation of API endpoints

#### Operations from the authorisation controller

**Operation:** User registration
**HTTP verb:** POST
**Path:** http://localhost:8080/auth/register
**Body:** 

```JSON
{
	"name": "Monique Mars",
	"email": "monique.mars@email.com",
	"user_name": "monique.mars",
	"password": "mm3436336"
}
```
**Auth:** None
**Response:**
```JSON
{
	"user_id": 4,
	"name": "Monique Mars",
	"user_name": "monique.mars"
}
```
Function registerd at ```auth_controller.py```. This function takes the information provided from the new user from the body, using the ```UserSchema``` validates that the format is in accordance to the entity, and it storages the details, creates the three bookshelves that each user should have ('Read', 'Reading', and 'To_read') and hashes the password. Finally, it commits and dumps the information, and it ends returning the info {"user_id", "name", ""user_name} in a JSON format.
In case that not nullable information is missing, the system returns a message declaring "Invalid email format" for email or "the column name is required" for other not nullable attributes.


**Operation:** User login
**HTTP verb:** POST
**Path:** http://localhost:8080/auth/login
**Body:** 
```JSON
{
	"email": "vittoria.vetra@email.com",
	"password": "user's password here"
}
```
**Auth:** None
**Response:**
```JSON
{
	"email": "vittoria.vetra@email.com",
	"is_admin": false,
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNzUwNTgyOSwianRpIjoiYTliYWE1ZWUtZjhjNC00YmZkLWFhNWYtN2FiZjZiNGRiNmU4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjIiLCJuYmYiOjE3Mjc1MDU4MjksImNzcmYiOiJjZTY4YTVkNi1kNTEwLTRkMDQtYWFjMS04OWIyZDIyOGJhZGIiLCJleHAiOjE3Mjc1OTIyMjl9.VCmb1PxTZaWcGryhesyA3B3TtoEdOQcjMMu7jocyd2Y"
}
```

Function registered in the ```auth_controller.py```. Once the user is properly registered in the database, the 'email' and 'password' of the user are taken from the body, and the function filters the entry by using the email. Then if the user exists, the password is checked using the bycrpt method and generates a response with {"email", "is_admin", "token"} in JSON format. If any of the previous authentication steps are not valid, the function returns a response with "Email or password incorrect".


**Operation:** Fetch all the users registered on the database
**HTTP verb:** GET
**Path:** http://localhost:8080/auth/users_profiles
**Body:** None
**Auth:** Admin Token
**Response:**

```JSON
[
	{
		"user_id": 1,
		"name": "Hernan Vela",
		"email": "hernan_admin@email.com"
	},
	{
		"user_id": 2,
		"name": "Vittoria Vetra",
		"email": "vittoria.vetra@email.com"
	},
	{
		"user_id": 3,
		"name": "Quino Qaro",
		"email": "quino.qaro@email.com"
	}
]
```

Function registered at ```auth_controller.py```. This operation uses the authorisation blueprint to establish the http route, and it uses the ```@auth_as_admin_decorator``` to check if the user performing this action is admin or not. If it is not admin, it returns a message suchs as "Only admin can perform this action", but if the user is an admin the function filters the database, make a list of all the users a returns it with {"user_id", "name", "email"}.


**Operation:** Amend user's information
**HTTP verb:** PUT, PATCH
**Path:** http://localhost:8080/auth/users_profiles/<int:user_id>
**Body:** 
```JSON
{
	"name":"Vittoria Aleko" (or any other key to be modified)
}
```
**Auth:** User's token
**Response:**
```JSON
{
	"user_id": 2,
	"name": "Vittoria Aleko",
	"user_name": "vittoria.vetra"
}
```

Function registered at ```auth_controller.py```. This operation can only be performed by the the user, so the function takes the token of the user to modify their own profile, and validate the portion of the user information that needs to be changed. Then it filters the ```users_profiles``` entity, finds the user and it modifies what is needed, to finally return the new information in a JSON format.
If the token information does not match, it returns "Missing Authorization Header", but if the user cannot be found or does not exist a messages is shown as "User does not exist".

Original entry:

```JSON
{
	"user_id": 2,
	"name": "Vittoria Vetra",
	"user_name": "vittoria.vetra"
}
```

Amended entry:

```JSON
{
	"user_id": 2,
	"name": "Vittoria Aleko",
	"user_name": "vittoria.vetra"
}
```


**Operation:** Delete a user
**HTTP verb:** DELETE
**Path:** http://localhost:8080/auth/users_profiles/<int:user_id>
**Body:** None
**Auth:** Admin token
**Response:**

```JSON
{
	"message": "User with id {int:user_id} is deleted."
}
```

Function registered at ```auth_controller.py```. This operation can only be performed by the the admin. The function takes the 'user_id' as argument, it filters the ```users_profiles``` entity by it, and it deletes the user when finds it. A message of acknowledgement is displayed as "User with id {user_id} is deleted".
If the user is not found a message is displayed as "User with id {user_id} not found."


#### Operation from the users_profiles controller

**Operation:** fetch all the stored books of any user
**HTTP verb:** GET
**Path:** http://localhost:8080/users_profiles/<int:user_id/bookshelves
**Body:** None
**Auth:** Toke of user doing the query
**Response:** (Example with user_id=2)

```JSON
[
	{
		"user": {
			"user_id": 2,
			"user_name": "vittoria.vetra"
		},
		"bookshelf_id": 4,
		"status": "read",
		"stored_books": [
			{
				"book": {
					"book_id": 2,
					"title": "Autobiography of a Yogi",
					"author": "Paramahansa Yogananda"
				}
			},
			{
				"book": {
					"book_id": 1,
					"title": "Requiem for a nun",
					"author": "William Faulkner"
				}
			}
		]
	},
	{
		"user": {
			"user_id": 2,
			"user_name": "vittoria.vetra"
		},
		"bookshelf_id": 5,
		"status": "reading",
		"stored_books": [
			{
				"book": {
					"book_id": 3,
					"title": "Flatland",
					"author": "Scott Atkins"
				}
			}
		]
	},
	{
		"user": {
			"user_id": 2,
			"user_name": "vittoria.vetra"
		},
		"bookshelf_id": 6,
		"status": "to-read",
		"stored_books": []
	}
]
```

Function registered at ```users_profiles_controller.py```. This query can be made by any user registered in the app. First, the function validates if the person doing the query is a user, by using the ```@jwt_required```.
Second, the function verifies that the user exists if not a message is displayed saying "User with id {user_id} does not exist". When the user exists, the program checks existence and ownership of the bookshelves, and it prompts a list of all the bookshelves with the stored books of the user requested in a JSON format.
Finally, if the bookshelves do not exist or the user is not the owner, a message is diplayed as "Bookshelves of user {user_id} cannot be found or user does not exist"


#### Operation from the bookshelves controller

**Operation:** Fetch a specific bookshelf
**HTTP verb:** GET
**Path:** http://localhost:8080/bookshelves/<int:bookshelf_id>
**Body:** None 
**Auth:** Token of user doing the query
**Response:** (Example with bookshelf_id=4)

```JSON
{
	"user": {
		"user_id": 2,
		"user_name": "vittoria.vetra"
	},
	"bookshelf_id": 4,
	"status": "read",
	"stored_books": [
		{
			"book": {
				"book_id": 2,
				"title": "Autobiography of a Yogi",
				"author": "Paramahansa Yogananda"
			}
		},
		{
			"book": {
				"book_id": 1,
				"title": "Requiem for a nun",
				"author": "William Faulkner"
			}
		}
	]
}
```

Function registered at ```bookshelves_controller.py```. Given that any registered user in the app can perform this operation, the function verify that the user is logged in with the ```jwt_required```. Then using the 'bookshelf_id' from the path, the program filter the 'bookshelves' entity to find the bookshelf and displays the information of the bookshelf.
When the bookshelf does not exist, a message is returned saying "Bookshelf {bookshelf_id} does not exist".


**Operation:** Add a book to a bookshelf
**HTTP verb:** POST
**Path:** http://localhost:8080/bookshelves/<int:bookshelf_id>/books/<int:book_id>
**Body:** 
```JSON
{
	"start_date": "2010-01-01"
}
```
**Auth:** Owner of the bookshelf
**Response:**
```JSON
{
	"message": "Book {<int:book_id>} added successfully to bookshelf {<int:bookshelf_id>}!"
}
```

Function registered at ```bookshelves_controller.py```. This function uses the ```@jwt_required``` to confirm that the person is a user registered in the app, and the ```get_jwt_identity``` to confirm that the user is the owner of the bookshelf where they pretend to add the book to. With the 'user_id' and the 'bookshelf_id' from the http path is checked existence and ownership, but if this is not the case, a message is shown as "Bookshelf not found or not owned by the user".
If existence and ownership are confirmed, the information is taken from the body, filterd thrhough with the 'StoredBook' as reference. When the book is already in the bookshelf a message is returned such as "Book {book_id} already exists in bookshelf {bookshelf_id}", to avoid duplicity of stored books.
If the book does not exist in the bookshelf, it is stored and an acknowledgement message is returned declaring "Book {book_id} added successfully to bookshelf {bookshelf_id}!"


**Operation:** Delete a book from a specific bookshelf
**HTTP verb:** DELETE
**Path:** http://localhost:8080/bookshelves/<int:bookshelf_id>/books/<int:book_id>
**Body:** None
**Auth:** Token of bookshelf owner
**Response:**

```JSON
{
	"message": "Book <int:book_id> deleted succesfully from bookshelf int:bookshelf_id>!"
}
```

Function registered at ```bookshelves_controller.py```. The function verifies that the person performing the deletion is the owner of the bookshelf by using ```jwt_required```. Then, the function takes the 'bookshelf_id' and 'user_id' and check existence and ownership of the shelf. If this is not true, a message is returned as "Bookshelf not found or not owned by the user".
Then, by using the 'bookshelf_id' and 'book_id' existence and ownership are checked. When it is confirmed the book is fetched through the StoredBook model,it is deleted, and a message is returned saying "Book {book_id} deleted succesfully from bookshelf {bookshelf_id}!".
If the book was not found in the bookshelf, a message is displayed saying "Book {book_id} coudln't be found in bookshelf {bookshelf_id}"


#### Operation from the book comments controller

**Operation:** Create a new comment of a book
**HTTP verb:** POST
**Path:** http://localhost:8080/books/<int:book_id>/book_comments
**Body:** 
```JSON
{
	"comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt."
}
```
**Auth:** Token of registered user
**Response:** (Example with book_id=1)
```JSON
{
	"user": {
		"user_id": 2,
		"user_name": "vittoria.vetra"
	},
	"book": {
		"book_id": 1,
		"title": "Requiem for a nun",
		"author": "William Faulkner"
	},
	"book_comment_id": 10,
	"date": "2024-09-29",
	"comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt."
}
```

Function registered at ```book_comments_controller.py```. Any registered user can make a comment on any existent book in 'books' entity. To do this, the function validates that the person making the comment is registered with ```@jwt_required```, then it takes the data from the body and loads it.
Next, with the 'book_id' the book is found using the Book model, and if it exists, the comment is taken and added to the 'book_comments' entity.
If the book_id does not exist, a message is displayed saying "Book with id {book_id} not found"


**Operation:** Amend an existent book comment
**HTTP verb:** PUT, PATCH
**Path:** http://localhost:8080/books/<int:book_id>/book_comments/<int:book_comment>
**Body:** 
```JSON
{
	"comment": "Only portion of comment entry that can be modified"
}
```

**Response:**(Example with user_id=6 and book_comment_id=18)

```JSON
{
	"user": {
		"user_id": 6,
		"user_name": "Curio Cassi"
	},
	"book": {
		"book_id": 1,
		"title": "Requiem for a nun",
		"author": "William Faulkner"
	},
	"book_comment_id": 18,
	"date": "2024-09-29",
	"comment": "Faulkner rocks."
}
```

Function registered at ```book_comments_controller.py```. The function uses the ```get_jwt_identity``` to confirm the user identity, then it checks with 'book_comment_id' whether the comment exists, and if 'user' owns such book comment. If it is not the case, a message is displayed saying "Comments can only be modified by the owner."
Next, the program confirms that 'user' only tries to modify the 'comment' field if not a error message is prompted as f"Invalid fields in the request. Only 'comment' can be modified."
Finally, if the program overcame the previous steps, the new comment is taken from the body, committed and return the new modified comment.

Original comment:
```JSON
{
	"user": {
		"user_id": 6,
		"user_name": "Curio Cassi"
	},
	"book": {
		"book_id": 1,
		"title": "Requiem for a nun",
		"author": "William Faulkner"
	},
	"book_comment_id": 18,
	"date": "2024-09-29",
	"comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt."
}
```

Amended comment:
```JSON
{
	"user": {
		"user_id": 6,
		"user_name": "Curio Cassi"
	},
	"book": {
		"book_id": 1,
		"title": "Requiem for a nun",
		"author": "William Faulkner"
	},
	"book_comment_id": 18,
	"date": "2024-09-29",
	"comment": "Faulkner rocks."
}
```

**Operation:** Delete a comment
**HTTP verb:** DELETE
**Path:** http://localhost:8080/books/<int:book_id>/book_comments/<int:book_comment_id>
**Body:** None
**Auth:** Token of comment owner
**Response:**
```JSON
{
	"message": "Book comment <int:book_comment_id> deleted successfully!"
}
```
Function registered at ```book_comments_controller.py```. The function uses ```get_jwt_identity``` to confirm the user identity. Then, the program takes the 'user_id' and 'book_comment_id' to determine existence and owenership of the comment. If the book comment is not found or the user is not the owner of the comment, a message is prompted saying "Book comment not found or not owned by the user."
Finally, if the program overcame these steps, the comment with 'book_comment_id' is deleted and an acknowledgement message is displayed as "Book comment {book_comment_id} deleted successfully!"


#### Operation from the book controller

**Operation:** fetch all the books in 'books' entity
**HTTP verb:** GET
**Path:** http://localhost:8080/books
**Body:** None
**Auth:** None
**Response:**
```JSON
[
	{
		"book_id": 1,
		"title": "Requiem for a nun",
		"author": "William Faulkner"
	},
	{
		"book_id": 2,
		"title": "Autobiography of a Yogi",
		"author": "Paramahansa Yogananda"
	},
	{
		"book_id": 3,
		"title": "Flatland",
		"author": "Scott Atkins"
	},
	{
		"book_id": 4,
		"title": "Life of Pi",
		"author": "Yann Martel"
	},
	{
		"book_id": 5,
		"title": "The Pill",
		"author": "James Sweet"
	}
]
```
Function registered at ```books_controller.py```. This function can be performed by any user of the platform, even by unregistered users.
It takes the request from the http path and returns a list of books in JSON format with {"book_id", "title", "author"}


**Operation:** Fetch a specific book with its comments from the 'books' entity
**HTTP verb:** GET
**Path:** http://localhost:8080/books/<int:book_id>
**Body:** None
**Auth:** None
**Response:**(Example with book_id=2)
```JSON
{
	"book_id": 2,
	"title": "Autobiography of a Yogi",
	"author": "Paramahansa Yogananda",
	"language": "English",
	"translator": "",
	"publisher": "Crystal Clarity Publishers",
	"publisher_city": "Chicago",
	"publication_date": "1946-05-05",
	"ebook_isbn": "9380590471004",
	"print_isbn": "9781565892125",
	"book_comments": [
		{
			"user": {
				"user_id": 3,
				"user_name": "quino.qaro"
			},
			"date": "2024-08-29",
			"comment": "This book became my lighthouse."
		},
		{
			"user": {
				"user_id": 1,
				"user_name": "hernan-vela"
			},
			"date": "2024-09-29",
			"comment": "It has a great narrative and a spiritual map of India."
		}
	]
}
```

Function registered at ```books_controller.py```. This function can be performed by any user of the platform, even by unregistered users. It takes the 'book_id' from the http path, and it looks into the database until the book is found. Then the book is displayed in a JSON format.
If the book_id is not found, the program returns a message as "Book with id {book_id} does not exist".

**Operation:** Add a new book
**HTTP verb:** POST
**Path:** http://localhost:8080/books
**Body:** 
```JSON
{
	"title": "The Pill",
	"author": "James Sweet",
	"language": "Portuguese",
	"translator": "Milk Sullivan",
	"publisher": "Cookie Inc",
	"publisher_city": "Hammerland",
	"publication_date": "2010-01-02",
	"ebook_isbn": "839303948490",
	"print_isbn": "6789097654536"
}
```
**Auth:** Admin token
**Response:**
```JSON
{
	"book_id": "34",
    "title": "The Pill",
	"author": "James Sweet",
	"language": "Portuguese",
	"translator": "Milk Sullivan",
	"publisher": "Cookie Inc",
	"publisher_city": "Hammerland",
	"publication_date": "2010-01-02",
	"ebook_isbn": "839303948490",
	"print_isbn": "6789097654536"
}
```

Function registered at ```books_controller.py```. This operation can only be performed by the admin, so the program uses ```@auth_as_admin_decorator``` to validate whether the user adding the book is an admin. If the user is not an admin, it returns a message as "Only admin can perform this action".
When the user is admin the data from the body is take, first the 'publication_date' is parsed and if it is not correctly loaded, a message explaining the format required is prompted. If the 'publication_date' is correct, the rest of the data from the body is taken according to Book model, then it is added, committed, and dumped in the 'book' entity.


**Operation:** Delete a book from the 'books' entity
**HTTP verb:** DELETE
**Path:** http://localhost:8080/books/<int:book_id>
**Body:** None
**Auth:** Admin token
**Response:**
```JSON
{
	"message": "Book <book_id> deleted successfully!"
}
```

Function registered at ```books_controller.py```. This operation can only be performed by the admin, so the program uses ```@auth_as_admin_decorator``` to validate whether the user deleting the book is an admin. If the user is not an admin, it returns a message as "Only admin can perform this action".
If the user is and admin, the program takes the 'book_id' from the http path, and it looks into the database until the book is found. Then the book is deleted and a message such as "Book {book_id} deleted successfully!"


**Operation:** Amend a book from the 'books' entity
**HTTP verb:** PUT, PATCH
**Path:** http://localhost:8080/books/<int:book_id>
**Body:** (Example below, but any key can be modified but 'book_id')

```JSON
{
	"publisher": "Random Random",
	"publisher_city": "Toronto"
}
```
**Auth:** Admin token
**Response:**

```JSON
{
	"book_id": 3,
	"title": "Flatland",
	"author": "Scott Atkins",
	"language": "English",
	"translator": "",
	"publisher": "Random Random",
	"publisher_city": "Toronto",
	"publication_date": "1955-01-01",
	"ebook_isbn": "2280590471004",
	"print_isbn": "2281565892125"
}
```

Function registered at ```books_controller.py```. This operation can only be performed by the admin, so the program uses ```@auth_as_admin_decorator``` to validate whether the user deleting the book is an admin. If the user is not an admin, it returns a message as "Only admin can perform this action".
The data is taken from the body of the request, loaded following the BookSchema and with 'partial=True' it allows the admin to modify some keys of the whole book entry.
Then the 'publication_date' is parsed and if the date format is not valid, a message such as "Expected format for publication_date is YYYY-MM-DD" is returned.
Next, the data from the body is compared with the original entry, and the keys to modified are changed. Finally, the system returns a the book information in a JSON format with the modified version.

Original entry:
```JSON
{
	"book_id": 3,
	"title": "Flatland",
	"author": "Scott Atkins",
	"language": "English",
	"translator": "",
	"publisher": "Geometry",
	"publisher_city": "Chicago",
	"publication_date": "1955-01-01",
	"ebook_isbn": "2280590471004",
	"print_isbn": "2281565892125"
}
```

Amended entry:
```JSON
{
	"book_id": 3,
	"title": "Flatland",
	"author": "Scott Atkins",
	"language": "English",
	"translator": "",
	"publisher": "Random Random",
	"publisher_city": "Toronto",
	"publication_date": "1955-01-01",
	"ebook_isbn": "2280590471004",
	"print_isbn": "2281565892125"
}
```



### Resources

[^flask]: Python Basics, 2021, *What is Flask Python*, accessed 27 Sep 2024, https://pythonbasics.org/what-is-flask-python/ 

[^os]: Geeks for Geeks, 2024, *OS Module in Python with Examples*, accessed 27 Sep 2024, https://www.geeksforgeeks.org/os-module-python-examples/

[^marshmallow]: Marhsmallow, 2024, *marshmallow: simplified object serialization*, accessed 27 Sep 2024, https://marshmallow.readthedocs.io/en/stable/

[^m.fields]: Marhsmallow, 2024, *Fields*, accessed 27 Sep 2024, https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html

[^bcrypt]: freeCodeCamp, 2024, *How to Hash Passwords with bcrypt in Node.js*, accessed 27 Sep 2024, https://www.freecodecamp.org/news/how-to-hash-passwords-with-bcrypt-in-nodejs/

[^jwt]: JWT, 2024, *Introduction to JSON Web Tokens*, accessed 27 Sep 2024, https://jwt.io/introduction

[^flask-kwt]: Flask, 2022, *Basic Usage*, accessed 27 Sep 2024, https://flask-jwt-extended.readthedocs.io/en/stable/basic_usage.html

[^sqlalchemy]: SQLAlchemy, 2024, *PostgreSQL*, accessed 27 Sep 2024, https://docs.sqlalchemy.org/en/20/dialects/postgresql.html

[^psql]: PostgreSQL 16 2024, Chapter 13. Concurrency Control, 13.1 Introduction, accessed 26 Sep 2024, https://www.postgresql.org/docs/current/mvcc-intro.html

[^A.Pavlo]: Andy Pavlo 2023, The Part of PostgreSQL We Hate the Most, accessed 27 Sep 2024, https://www.cs.cmu.edu/~pavlo/blog/2023/04/the-part-of-postgresql-we-hate-the-most.htm