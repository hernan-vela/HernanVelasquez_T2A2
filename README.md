# Coder Academy Full Stack Web Development Diploma
## HernanVelasquez_T2A2 
## API Server


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

**Operation:** 
**HTTP verb:** 
**Path:** 
**Body:** 
**Auth:** 
**Response:**

**Operation:** 
**HTTP verb:** 
**Path:** 
**Body:** 
**Auth:** 
**Response:**



#### Operation on 'books' entity

**Operation:** Fetch the whole library
**HTTP verb:** GET
**Path:**  http://localhost:8080/books
**Body:** None
**Response:** 
```
[
{

    "book_id": "<int1>",
    "title": "Story book",
    "author": "Famous writer 1"
},
{
    "book_id": "<int2>",
    "title": "Story book",
    "author": "Famous writer 2" 

},
{
    "book_id": "<int3>",
    "title": "Story book",
    "author": "Famous writer 2" 

},
{
    "book_id": "<int4>",
    "title": "Story book",
    "author": "Famous writer 3" 

}
]
```

Function registered in ```books_controller.py```. 


**Operation:** Fetch a specific book
**HTTP verb:** GET
**Path:**  http://localhost:8080/books/<int:book_id33>
**Body:** None
**Auth:** user Token
**Response:** 
```
{
    "book_id": "<int:book_id33>,
    "title": "The Reader",
    "author": "Rainer Maria Rilke",
    "language": "German",
    "translator": "Erne Raim",
    "publisher": "Scholastic",
    "publisher_city": "Caana",
    "publication_date": "1980",
    "ebook_isbn": "0989765678987",
    "print_isbn": "6667876545679"
}
```

Function registered in ```books_controller.py```. 


**Operation:** Create a book
**HTTP verb:** POST
**Path:**  http://localhost:8080/books/
**Body:**

```
{
    "title": "R",
    "author": "Runt Runta",
    "language": "English",
    "translator": "",
    "publisher": "Echo Books",
    "publisher_city": "New York",
    "publication_date": "1999",
    "ebook_isbn": "0989755678987",
    "print_isbn": "2667876545679"
}
```
**Auth:** admin Token
**Response:** 
```
{
    "Book with id {book_id} has been added"
}
```


Function registered in ```books_controller.py```. 



**Operation:** Delete a book
**HTTP verb:** DELETE
**Path:**  http://localhost:8080/books/<int:book_id>
**Body:** None
**Auth:** admin Token
**Response:** 
```
{
    "Book with id {book_id} has been deleted."
}
```

Function registered in ```books_controller.py```. 


**Operation:** Append a book
**HTTP verb:** PUT, PATCH
**Path:**  http://localhost:8080/books/<int:book_id>
**Body:**
```
{
    "publication_date": "2001",
}
```

**Auth:** admin Token
**Response:** 

```
{
    "title": "The Endless Story",
    "author": "Brito Gallag",
    "language": "English",
    "translator": "",
    "publisher": "Echo Books",
    "publisher_city": "Toscana",
    "publication_date": "2001",
    "ebook_isbn": "3489755678987",
    "print_isbn": "5667876545679"
}
```

Function registered in ```books_controller.py```. 


Original entry:

```
{
    "title": "The Endless Story",
    "author": "Brito Gallag",
    "language": "English",
    "translator": "",
    "publisher": "Echo Books",
    "publisher_city": "Toscana",
    "publication_date": "1967",
    "ebook_isbn": "3489755678987",
    "print_isbn": "5667876545679"
}
```

Updated entry:

```
{
    "title": "The Endless Story",
    "author": "Brito Gallag",
    "language": "English",
    "translator": "",
    "publisher": "Echo Books",
    "publisher_city": "Toscana",
    "publication_date": "2001",
    "ebook_isbn": "3489755678987",
    "print_isbn": "5667876545679"
}
```


#### Operations on 'bookshelves' entity

**Operation:** Fetch all the bookshelves of a user
**HTTP verb:** GET
**Path:** http://localhost:8080/bookshelf
**Body:** None
**Response:** 
```
{
	"user_id": "<int1>",
	"user_name": "John Doe",
	"bookshelves": [
        {
            "bookshelf_id": "<int2>",
            "status": "Read",
            "start_date": "2021-10-11",
            "end_date": "",
            "review": "Opinion bout book"
        },
        {
            "bookshelf_id": "<int3>",
            "title": "Name_of_the_book",
            "author": "author_of_book,
            "status": "To-read",
            "start_date": "2021-01-09",
            "end_date": "",
            "review": "Opinion about book"
        },
        {
            "bookshelf_id": "<int4>",
            "title": "Name_of_the_book",
            "author": "author_of_book,
            "status": "Reading",
            "start_date": "2021-10-10",
            "end_date": "",
            "review": "Opinion about book"
        }
    ]
}
```
Function registered in the ```bookshelves_controller.py```, this function validates the user with the ```jwt_required```, and it returns a list with the user name, ```user_id``` and all the bookshelves created by the user.

**Operation:** Fetch all books on the same bookshelf
**HTTP verb:** GET
**Path:** http://localhost:8080/users_profiles/<int:user_id>/bookshelves/<status>/books
**Body:** None
**Response:** 
```
{
	"user_id": "<int1>",
	"bookshelf_id": "<int1>, # Reading
    "books": [
        {
            "book_id": "3",
            "title": "Flatland",
            "author": "Scoot Atkins",
            "start_date": "2024-07-01"
            "end_date": "",
            "review": ""
        },
        {
            "book_id": "4"
            "title": "The adventures of Tom Sawyer"
            "author": "Mark Twain",
            "start_date": "2024-07-12"
            "end_date": "",
            "review": ""
        }
    ]
}
```    






         


Function registered in the ```bookshelves_controller.py```.....from status "Reading"

**WILL THIS OPERATION ADD A BOOKSHELF**



**Operation:** Add a book to a bookshelf
**HTTP verb:** POST
**Path:** http://localhost:8080/bookshelf/<int:bookshelf_id>/book/<int:book_id>
**Body:** None
**Auth:** user Token
**Response:** 
```
{"Bookshelf with book {title} was successfully added!"}
```

Function registered in the ```bookshelves_controller.py```


**WHAT WOULD IT HAPPEN IF THE URL IS THE SAME AS DELETE BOOKSHELF**

**Operation:** Delete a bookshelf
**HTTP verb:**  DELETE
**Path:** http://localhost:8080/bookshelf/<int:bookshelf_id>
**Body:** None
**Auth:** user Token
**Response:** 
```
{"Your bookshelf {bookshelf_id} has been deleted!"}
```
Function registered in the ```bookshelves_controller.py```



**Operation:** Update an existent bookshelf of a user
**HTTP verb:** PUT, PATCH
**Path:** http://localhost:8080/bookshelf/<int:bookshelf_id>
**Body:** Only bookshelves with "Reading" and "To-read" statuses can be changed.
```JSON
{
   "status": "Read",
   "end_date": "2021-03-25"
}
```
**Auth:** user Token
**Response:** 
```
{
    "status": "Read",
    "end_date": "2021-03-25",
    "review": "Updated opinion about the book"
}
```
Function registered in the ```bookshelves_controller.py```

Original bookshelf entry:
```
{
   "bookshelf_id": "<int4>",
    "title": "Name_of_the_book",
    "author": "author_of_book,
    "status": "Reading",
    "start_date": "2024-10-04",
    "end_date": "",
    "review": "Opinion about book"
}
```

Updated bookshelf entry:
```{
    "bookshelf_id": "<int3>",
    "title": "Name_of_the_book",
    "author": "author_of_book,
    "status": "Read",
    "start_date": "2021-01-09",
    "end_date": "2021-03-25",
    "review": "Updated opinion about the book"
}
```




**Operation:** 
**HTTP verb:** 
**Path:** 
**Body:**
```JSON
{
   
}
```
**Auth:** 
**Response:** 
```
{

}
```
Function registered in the ```auth_controller.py```


