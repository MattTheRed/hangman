***********
Hangman
***********

A web app for playing hangman


************
Installation
************

Clone the repo from x

Create a virtualenv and install requirements

::

    $ pip install -r requirements.txt

Create the database
::
    $ python manage.py syncdb


************
Roadmap
************

models
    user
        get_score()

    words
        name
    game
        word
        user
        guesses_count

views
    register - django-registration?


rest api or forms?
    django-rest-framework?

    user/1/games
    user/1/games/create
    user/1/games/1
    user/1/games/1/guess


scability
    deploy on heroku
    replace sqlite w/ postgres
    static resources on S3
    memcache for templates, sessions, etc



