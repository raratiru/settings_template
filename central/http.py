#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

from decouple import config


ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

STATIC_ROOT = Path(config("POET_PROJECT_PATH")) / "www" / "static"
MEDIA_ROOT = Path(config("POET_PROJECT_PATH")) / "www" / "media"

STATIC_URL = "static/"
MEDIA_URL = "media/"

STATICFILES_DIRS = [
    Path(config("POET_DJANGO_PROJECT_PATH")) / "static",
    Path(config("POET_DJANGO_PROJECT_PATH")) / "theme" / "static",
]
