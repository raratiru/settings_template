#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decouple import config

START_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.sites",
)

LOCAL_APPS = ()

OTHER_APPS = (
    "people",
    "theme",
)

INSTALLED_APPS = START_APPS + LOCAL_APPS + OTHER_APPS

DATABASES = {
    "default": {
        "ENGINE": config(
            "POET_DJANGO_DATABASE_MAIN_ENGINE", default="django.db.backends.postgresql"
        ),
        "NAME": config("POET_DJANGO_DATABASE_MAIN_NAME"),
        "USER": config("POET_DJANGO_DATABASE_MAIN_USER"),
        "PASSWORD": config("POET_DJANGO_DATABASE_MAIN_PASSWORD"),
        "HOST": config("POET_DJANGO_DATABASE_MAIN_HOST", default="localhost"),
        "PORT": config("POET_DJANGO_DATABASE_MAIN_PORT", default="5432"),
    }
}

SITE_ID = 1
ROOT_URLCONF = "main.urls"
