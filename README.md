# API Project | Books

This project creates with the Django framework. I am using Postgres database.
I created an API book project where you can add new books, add them to favorites, rate and write reviews. 
![Link](https://github.com/uzhegovaelena/books-api/blob/main/Book.PNG)

You can filter by favorites and ratings.  
![Link](https://github.com/uzhegovaelena/books-api/blob/main/Favorites.PNG)

I also installed the admin panel.
![Link](https://github.com/uzhegovaelena/books-api/blob/main/admin.PNG)

## Backend development workflow

```shell
virtualenv env
./venv/Scripts/activate
python manage.py runserver
```

- Create database books_api
- Create admin
```shell
python manage.py createsuperuser
```

- GET/POST: http://127.0.0.1:8000/api/books/


