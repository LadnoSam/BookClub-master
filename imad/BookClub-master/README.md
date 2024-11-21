# BookClub [![Build Status](https://travis-ci.org/stephenfeagin/BookClub.svg?branch=master)](https://travis-ci.org/stephenfeagin/BookClub)

**Django app for book reviews and discussions**

This project is a web app that allows users to share the books that they are reading, 
create lists of books they have already read or are planning to read, and write reviews
of books. Future iterations will allow for creation of groups, whereby users can discuss
books together and plan future readings.

## Tech Stack

BookClub is built primarily with Django (Python 3.6+), using Bootstrap for some basic styling.

## Installation

To install this application, first clone the git repository:

```bash
git clone https://github.com/stephenfeagin/BookClub.git
```

Then, create a virtual environment and install the dependencies:

```bash
python -m venv venv
venv/bin/activate
install --upgrade pip
install -r requirements.txt
```

Then deploy it using Django's built-in server:

```bash
python manage.py runserver
```

## Attribution

I followed an [article at testdriven.io](https://testdriven.io/blog/django-custom-user-model/) on creating a custom
user model in Django.
