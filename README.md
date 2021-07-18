# A Weather Map app

<p align="left">
<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://pycqa.github.io/isortE"><img alt="Imports: isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

<p align="center">
  <img src="https://raw.github.com/marcosvbras/todo-list-python/master/images/to-do-list.jpg" alt="Custom image"/>
</p>


## What is this?
This is a **TodoGARPIX** was completed as part of the test task when applying for an internship at GARPIX.


## What can?
- see the list of tasks
- create a new task
- detailed task overview
- change one task
- delete task


## Environment
Env file in the root of the project and add the following (example) to it:
```
FLASK_APP=run.py
FLASK_ENV=testing

SECRET_KEY=secretsecretsecretsecretsecretsecretsecretsecretsecret
POSTGRES_DB=db
POSTGRES_USER=post
POSTGRES_PASSWORD=post
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```


## Getting started
clone:
```
$ git clone https://github.com/AlexKhlybov/TodoGARPIX.git
$ cd TodoGARPIX
```
create & activate virtual env then install dependency

with venv/virtualenv + pip:
```
$ python3 -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```

We carry out migrations:
```
$ alembic upgrade head
```

To run the program, type in the console:
```
$ uvicorn main:app --reload
```

Add records to the database.
First, let's go to [Swagger UI](http://127.0.0.1:8000/docs#/default/town_create_api_town__post).
You can copy the entries below or enter your cities:
```
{
    "name": "Ufa",
    "longitude": 56.4,
    "latitude": 54.49
}
{
    "name": "Moskow",
    "longitude": 37.37,
    "latitude": 55.45
}
{
    "name": "Izhevsk",
    "longitude": 53.13,
    "latitude": 56.51
}
```

To view the weather forecast for the entered cities, go to the main page - [Home page](http://127.0.0.1:8000)



## REST-API interactions
Use [Swagger UI](https://swagger.io/tools/swagger-ui/) or [cUrl](https://curl.se/) utility to manipulate towns. Below is an example of using the cUrl utility:

**GET the List of towns**
```
curl -H 'Content-Type: application/json' -X 'GET' 'http://127.0.0.1:8000/api/town/'
```

**GET an individual todo**
```
curl -H 'Content-Type: application/json' -X 'GET' 'http://127.0.0.1:8000/api/town/{town_id}'
```

**POST a todo**
```
curl -H 'Content-Type: application/json' -d '{"title":"Dinner", "content":"Having Dinner"}' -X 'POST' 'http://127.0.0.1:8000/api/town/'
```

**UPDATE a todo**
```
curl -H 'Content-Type: application/json' -d '{"title":"Dinner", "content":"Having Dinner"}' -X 'PUT' 'http://127.0.0.1:8000/api/town/{town_id}'
```

**DELETE a todo**
```
curl -H 'Content-Type: application/json' -X 'DELETE' 'http://127.0.0.1:8000/api/town/{town_id}'
```


## UnitTEST
To run the tests, you can use [unittest2](https://pypi.org/project/unittest2/) as following:

First, let's change the mode to test, to do this, in the `.env` file, replace the value of the `FLASK_ENV` variable:
```
...
FLASK_ENV=testing
...
```

Next, we raise the application with the command familiar to us:
```
$ flask run
```

```bash
$ python3 -m unittest discover tests
.......
----------------------------------------------------------------------
Ran 7 tests in 0.200s

OK
```


## ATTENTION! 
To run in development mode, replace the variable with `development`:
```
...
FLASK_ENV=development
...
```


## License
MIT
