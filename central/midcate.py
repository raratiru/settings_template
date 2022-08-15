#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

from decouple import config


CACHES = {
    "default": {
        "BACKEND": "diskcache.DjangoCache",
        "LOCATION": Path(config("POET_PROJECT_PATH")) / "www" / "cache",
        "SHARDS": 8,
        "DATABASE_TIMEOUT": 1.0,  # DiskCache transaction timeout (retry=True)
        "TIMEOUT": 12 * 60 * 60,  # 12 hours. Sessions are cached for this long.
        "VERSION": 1,
        "OPTIONS": {
            "size_limit": 2**32,  # 4 gigabytes
            "MAX_ENTRIES": 15000,
            "CULL_FREQUENCY": 3,  # Wipe 1/3 of the database on hitting a limit.
        },
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.http.ConditionalGetMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",  # #
                "django.template.context_processors.media",  # #
                "django.template.context_processors.static",  # #
                "django.template.context_processors.tz",  # #
            ],
        },
    },
]
