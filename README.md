# go²people websites challenge

Assignment for Django developer internship

---

## Getting Started

This project requires **[Python3](https://www.python.org)** and [Django](https://www.djangoproject.com) to build, if they are not installed on your device, you should install them first.

### Install dependencies

```sh
pip install -r requirements.txt
```

### Initial server setup

> If you have done the setup before; skip to [Starting the local server](#starting-the-local-server)

#### 1. Create Django Database

```sh
./manage.py makemigrations
./manage.py migrate
```

#### 2. Create test user

```sh
./manage.py createsuperuser
```

> Then follow the instructions on your command line terminal to create a superuser account.

#### 3. Load dummy data into the database

```sh
./manage.py loaddata dummyData.json

```

### Starting the local server

#### 1. Running the server

```sh
./manage.py runserver
```

#### 2. Running tests

```sh
./manage.py test
```

### Accessing the website

The website can be accessed by visiting the URL [localhost:8000](localhost:8000)

### Admin dashboard

Server admin dashboard can be accessed by visiting the URL [localhost:8000/admin](localhost:8000/admin)

---

## Project structure

```txt
├── go2people           :global project
│   ├── settings.py     :global settings
│   └── urls.py         :global urls
├── manage.py           :Django's CLI utility
├── media               :media storage location
├── shop                :shop app
│   ├── apps.py         :app config
│   ├── admin.py        :app admin config
│   ├── models.py       :models
│   ├── tests.py        :unit tests
│   ├── urls.py         :app urls
│   └── views.py        :app views
├── templates           :app html templates
└── db.sqlite3          :project database
```
