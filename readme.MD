***********
Hangman
***********
A web app for playing hangman. Demo at: http://hangman5000.herokuapp.com/

Login with the username/password m/m

************
Installation
************

Clone the repo from
```
    $ git clone git@github.com:MattTheRed/hangman.git
```
Create a virtualenv and install requirements
```
    $ pip install -r requirements.txt
```
Run the webserver
```
    $ python manage.py runserver
```
Login with the username/password m/m

************
Roadmap
************

This is just a simple demo app. For a production app I would:
* Switch from sqlite to a PostGreSQL or MySQL (nor keep the DB in source control)
* Add a registration process instead of using the django admin authentication
* Switch the proxy user model to a custom user model
* Add validation to my api
* Add csrf protection to the api

To scale the app to 1 million users:
* Deploy on Heroku (expensive), Amazon (Elastic Beanstalk), or Google App Engine
* Use Memcached to do caching of html templates, cache select database queries
* Move sessions storage from the database into memcached
* Move static assets into S3 and put them behind CloudFront
* Minify static assets and gzip them
* Possibly do full static page caching with Varnish or CloudFront
* Use a hosted database like RDS or Amazon's PostGreSQL offering that can handle
    many concurrent connections, do database sharding, and connection pooling






