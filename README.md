# API Project | Books

## Technology stack:
- Python 3.8.5
- Django 3.2.7
- PostgreSQL 5.2

## Сommands to start the service:
- python -m venv
- .\books_api\Scripts\activate
- pip install -r requirements.txt
- python manage.py runserver
- create admin: python manage.py createsuperuser

## Database:
- Create database books_api

## Enviroment variables: 
```
PORT=8000

# variables for DB connection:
DB_DATABASE=books_api
DB_USER=replace_me
DB_PASSWORD=replace_me
DB_HOST=localhost
DB_PORT=5432
```

## Endpoints

#### Add a new book

```
curl --request POST \
  --url http://127.0.0.1:8000/api/books/ \
  --header 'Content-Type: application/json' \
  --data '{
    "title": "New title",
    "author": "New author",
    "reviews": "Write a review"
  }'
```

#### Get list of books

```
curl --request GET \
  --url http://127.0.0.1:8000/api/books
```

#### Get a book

```
curl --request GET \
  --url http://127.0.0.1:8000/api/books/[book_id]
```


### Edit book:
![Link](https://github.com/uzhegovaelena/books-api/blob/main/Book.PNG)

### Filter by favorites and ratings:  
![Link](https://github.com/uzhegovaelena/books-api/blob/main/Favorites.PNG)

### Admin panel:
![Link](https://github.com/uzhegovaelena/books-api/blob/main/admin.PNG)
