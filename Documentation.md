# Coder Academy Full Stack Web Development Diploma
## HernanVelasquez_T2A2 
## API Server


### Operation of API endpoints

#### Users operations

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



**Operation:**
**HTTP verb:**
**Path:**  http://localhost:8080/
**Body:**

```JSON
{
   
}
```
**Response:** 


#### Operations on 'bookshelves' entity

**Operation:** Fetch all the bookshelves of a user
**HTTP verb:** GET
**Path:** http://localhost:8080/users_profiles/<int:user_id>/bookshelf
**Body:** None
**Response:** 
```
{
	"user_id": "<int1>",
	"user_name": "John Doe",
	"bookshelves": [
        {
            "bookshelf_id": "<int2>",
            "title": "Name_of_the_book",
            "author": "author_of_book,
            "status": "Reading",
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

**Operation:** Fetch all the bookshelves of a user with the same status.
**HTTP verb:** GET
**Path:** http://localhost:8080/users_profiles/<int:user_id>/bookshelves/<status>
**Body:** None
**Response:** 
```
{
	"user_id": "<int1>",
	"user_name": "John Doe",
	"bookshelves": [
        {
            "bookshelf_id": "<int2>",
            "title": "Name_of_the_book",
            "author": "author_of_book,
            "status": "Reading",
            "start_date": "2024-10-02",
            "end_date": "",
            "review": "Opinion bout book"
        },
        {
            "bookshelf_id": "<int3>",
            "title": "Name_of_the_book",
            "author": "author_of_book,
            "status": "Reading",
            "start_date": "2024-01-03",
            "end_date": "",
            "review": "Opinion about book"
        },
        {
            "bookshelf_id": "<int4>",
            "title": "Name_of_the_book",
            "author": "author_of_book,
            "status": "Reading",
            "start_date": "2024-10-04",
            "end_date": "",
            "review": "Opinion about book"
        }
    ]
}
```


Function registered in the ```bookshelves_controller.py```.....from status "Reading"

**WILL THIS OPERATION ADD A BOOKSHELF**



**Operation:** Add a bookshelf
**HTTP verb:** POST
**Path:** http://localhost:8080/users_profiles/bookshelf
**Body:**
```JSON
{
    "title": "Flatland: A Romance in Many Dimensions",
    "author": "Edwin Abbott",
    "status": "Read",
    "start_date": "2021-02-03",
    "end_date": "2021-02-04",
    "review": "I never thought about laughing at reading mathematics."
}
```
**Auth:** user Token
**Response:** 
```
{"Bookshelf with book {title} was successfully added!"}
```

Function registered in the ```bookshelves_controller.py```


**WHAT WOULD IT HAPPEN IF THE URL IS THE SAME AS DELETE BOOKSHELF**

**Operation:** Delete a bookshelf
**HTTP verb:**  DELETE
**Path:** http://localhost:8080/users_profiles/<int:user_id>/bookshelf/<int:bookshelf_id>
**Body:** None
**Auth:** user Token
**Response:** 
```
{"Your bookshelf {bookshelf_id} has been deleted!"}
```
Function registered in the ```bookshelves_controller.py```



**Operation:** Update an existent bookshelf of a user
**HTTP verb:** PUT, PATCH
**Path:** http://localhost:8080/users_profiles/<int:user_id>/bookshelf/<int:bookshelf_id>
**Body:** Only bookshelves with "Reading" and "To-read" statuses can be changed.
```JSON
{
   "status":
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


