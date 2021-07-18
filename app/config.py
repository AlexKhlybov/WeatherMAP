import os
from os.path import dirname, abspath

from dotenv import load_dotenv

BASEDIR = abspath(dirname(__file__))

DB_NAME = "weather_db.db"
DB_NAME_TEST = "test_db.db"

load_dotenv()
YANDEX_KEY = os.getenv("YANDEX_KEY")
WEATHER_LANG = os.getenv("WEATHER_LANG")
TESTING = os.getenv('TESTING')


