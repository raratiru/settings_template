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
    "people.apps.PeopleConfig",
    "theme",
    # "django.contrib.sites",
]

DATABASES = {
    "default": {
        "ENGINE": config("POET_DATABASE_ENGINE", default="django.db.backends.postgresql"),
        "NAME": config("POET_DATABASE_NAME"),
        "USER": config("POET_DATABASE_USER"),
        "PASSWORD": config("POET_DATABASE_PASSWORD"),
        "HOST": config("POET_DATABASE_HOST", default="localhost"),
        "PORT": config("POET_DATABASE_PORT", default="5432"),
    }
}

SITE_ID = 1
ROOT_URLCONF = "main.urls"
