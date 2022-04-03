#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decouple import config


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POET_DATABASE_NAME"),
        "USER": config("POET_DATABASE_USER"),
        "PASSWORD": config("POET_DATABASE_PASSWORD"),
        "HOST": "localhost",
        "PORT": "5432",
    }
}

AUTH_USER_MODEL = "people.User"
DEBUG = True
SECRET_KEY = config("POET_SECRET_KEY")
SITE_ID = 1
