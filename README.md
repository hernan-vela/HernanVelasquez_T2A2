# Coder Academy Full Stack Web Development Diploma
## HernanVelasquez_T2A2 
## API Server


### Allocation and tracking of tasks throuhout the API project

Considering the timeframe, and workload for my skills and priorities, the project was planned with 5 main stages, as follows: draft models, draft controllers, complete CRUD operations for app features, test endopoints and debugging until endpoints work flawlessly. The layout of the project plan can be witnessed in **Trello** where the cards show deadlines, and additional checklists to detail each stage.




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
	"book_comment_id": 12,
	"date": "2024-08-10",
	"comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt."
}
```

Function registered at ```book_comments_controller.py```. Any registered user can make a comment on any existent book in 'books' entity. To do this, the function validates that the person making the comment is registered with ```@jwt_required```, then it takes the data from the body and loads it according to the book schema.
Next, with the 'book_id' in the http path, the book is found using the Book model, and if it exists, the comment is taken and added to the 'book_comments' entity.
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
**Response:**


**Operation:** 
**HTTP verb:** 
**Path:** 
**Auth:**
**Response:**





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


**Operation:** Fetch a specific book from the 'books' entity
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
	"print_isbn": "9781565892125"
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
