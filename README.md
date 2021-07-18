# A Weather Map app

<p align="left">
<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://pycqa.github.io/isortE"><img alt="Imports: isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

![Screenshot](icon.png)


## What is this?
An application with the functionality of obtaining weather data by coordinates via API from a third-party service.


## What can?
- see the list of town
- create a new town
- detailed town overview
- change one town
- delete town


## Environment
Env file in the root of the project and add the following (example) to it:
```
TESTING=False

WEATHER_LANG="ru-RU"
YANDEX_KEY="BigSecret!!!"
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


## Pytest
To run the tests, you can use [pytest](https://docs.pytest.org/) as following:

First, let's change the mode to test, to do this, in the `.env` file, replace the value of the `TESTING` variable:
```
...
TESTING=True
...
```

Next, we raise the application with the command familiar to us:
```
$ pytest
```

```bash
$ pytest
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/macak/Documents/py_proj/WeatherMAP
collected 9 items                                                              

tests/test_api.py .........                                              [100%]

============================== 9 passed in 1.08s ===============================
```


## ATTENTION! 
To run in development mode, replace the variable with `False`:
```
...
TESTING=False
...
```


## License
MIT
