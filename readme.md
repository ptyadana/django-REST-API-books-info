# Books Info REST API Project

A simple REST API for getting the lists of books information using 
+ Python 3
+ Django 3
+ Django REST framework

[Visit BooksInfo API on heroku](https://booksbyptyadana.herokuapp.com/books/)
### Base URL
base URL for all endpoints: ```https://booksbyptyadana.herokuapp.com/```

### Endpoints
```/books``` get all books

#### Sample JSON
```javascript
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "book_name": "Flip It: How to Get the Best Out of Everything",
        "author_name": "Michael Heppell",
        "book_price": 15,
        "book_quantity": 1000
    },
    {
        "id": 2,
        "book_name": "Harry Potter Paperback Box Set (Books 1-7)",
        "author_name": "J. K. Rowling",
        "book_price": 55,
        "book_quantity": 71
    }
]
```