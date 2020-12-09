# User-authentication using Django:
It is a basic applicaion in which following operations can be performed:

    - user signup via email/user name : http://127.0.0.1:8000/accounts/signup/
    - signin/login : http://127.0.0.1:8000/accounts/login/
    - signout/logout : http://127.0.0.1:8000/accounts/logout/
    - forget password : http://127.0.0.1:8000/accounts/reset_password/ 
    - update password : http://127.0.0.1:8000/accounts/change_password/
    - user profile edit : http://127.0.0.1:8000/accounts/update_user/

# Technology stack:
1. Python3
2. Django REST Framework
3. sqlite3 Database

# Project Structure:
```
.
├── accounts
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── templates
│   ├── base.html
│   ├── home.html
│   └── registration
│       ├── change_password.html
│       ├── login.html
│       ├── password_reset_complete.html
│       ├── password_reset_confirm.html
│       ├── password_reset_done.html
│       ├── password_reset_form.html
│       ├── signup.html
│       └── update_user.html
│   ├── base.html
│   ├── home.html
│   └── registration
└── user_auth_project
    ├── __init__.py
    ├── __pycache__
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

# Running Locally:
First, clone the repository to your local machine:

git clone https://github.com/saiyadfaizan/user_authentication_django.git

cd user_auth_project

# Create super user:
python manage.py createsuperuser 

Note: It will prompt to enter username, email and password one by one. Please remember the username and password,
it will be used to login admin area.

# Steps to run the project:
1. Install the requirements: pip install -r requirements/dev.txt
2. Check for the database migrations: python manage.py makemigrations
3. Apply the database migrations: python manage.py migrate
4. Run the developement server: python manage.py runserver
5. Open chrome and the site will be available at 127.0.0.1:8000.
