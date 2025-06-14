# pip install python-decouple
from decouple import config as decouple_config

DB_URL = decouple_config("DB_URL", default="")