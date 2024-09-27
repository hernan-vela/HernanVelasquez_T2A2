# Coder Academy Full Stack Web Development Diploma
## HernanVelasquez_T2A2 
## API Server


### Operation of API endpoints

#### Operation on 'users_profiles' entity

**Operation:** Register User
**HTTP verb:** POST
**Path:** http://localhost:8080/auth/register
**Body:**

```JSON
{
    "name": "John Doe",
	"email": "john.doe@email.com",
	"user_name": "john.doe",
	"password": "jd3436336"
}
```
**Response:**

**PENDING**

Function registered in ```auth_controller.py```. It takes the information from the front end according to the ```UserSchema``` (see Body for details), it hashes the user's password using bycrypt, it adds the information to the database, commits the data and dumps the data.
In case of missing the email from the user it returns an error such as "Email address is required", but if another not nullable attribute is missing it returns an error message as "The column ```missing_attribute``` is required".


**Operation:** User login
**HTTP verb:** POST
**Path**: http://localhost:8080/auth/login
**Body**:
```JSON
{
    "email": "john.doe@email.com",
    "password": "jd3436336"
}
```
**Response:** 
```
{
	"email": "john.doe@email.com",
	"is_admin": false,
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNzE3ODcyOCwianRpIjoiNmQyZmNkZTctZjg0Ni00MTliLWE2NDMtNGY3YjYwMWRmMWJhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE3MjcxNzg3MjgsImNzcmYiOiI1Njg4MThlMC00ODA1LTQ3ZDQtOWJiNy1mYzNkNDZjMzM0ZDEiLCJleHAiOjE3MjcyNjUxMjh9.Hrthgg8JaTvaxaQJ65DIyItGSq4tubuAlOTeJk3K7bY"
}
```
Function registered in the ```auth_controller.py```. Once the user is properly registered in the databasae, the 'email' and 'password' of the user are taken from the front end, and the function filters the entry by using the email. Then if the user exists, the password is checked using the bycrpt method and generates a response with 'email', 'is_admin' and an authentication token. If any of the previous authentication steps are not valid, the function returns a response with "Email or password incorrect".

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


