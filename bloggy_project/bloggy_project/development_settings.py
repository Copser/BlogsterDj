# -*-coding: utf-8-*-
from .settings import *
import os

DEBUG = True
# TEMPLATE_DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "bloggy_db",
        "USER": "petarp",
        "PASSWORD": "gnomeregan",
        "HOST": "",
        "PORT": "",
    }
}
