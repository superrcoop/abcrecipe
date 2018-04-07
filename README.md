# abcrecipe.xyz

Description
-------------------

Recipe and meal planner

Getting Started !
-------------------

This Web app requires the latest version of [Python and Flask](http://flask.pocoo.org)

Clone the repository:

`$ git clone https://github.com/superrcoop/abcrecipe.git`

Go into the repository:

`$ cd abcrecipe`

Create virtual environment(activate):

`$ virualenv venv
 $ source venv/bin/activate`

Install dependencies:

`$ pip install -r requirements.txt`


Deploy
--------

To test locally,Ensure that [PostgreSQL](https://www.postgresql.org/docs/8.0/static/tutorial-start.html) or [MySql](https://dev.mysql.com/doc/mysql-getting-started/en/) is installed and running and configure the database URI located in `__init__.py`

Locally: 

~~~~python
app.config['SQLALCHEMY_DATABASE_URI'] =  '<database_url>'
~~~~

Setup database: 

~~~
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
~~~

Run:

`$ python run.py`