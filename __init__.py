#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import environ
from pathlib import Path

from decouple import config
from main.settings.concord import concord_settings
from main.settings.gears import gears_settings
from split_settings.tools import include, optional

AUTH_USER_MODEL = "people.User"
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEBUG = False
SECRET_KEY = config("POET_DJANGO_SECRET_KEY")

# Managing environment:
environ.setdefault("POET_ENV", "Dev")
env_choices = {
    "Dev": "development",
    "Prod": "production",
    "Alt": "alternate",
}
_ENV = env_choices[environ["POET_ENV"]]
_base_settings = filter(
    None,
    (
        "central/base.py",
        "central/authentication.py",
        "central/communication.py",
        "central/csp.py",
        "central/http.py",
        "central/localization.py",
        "central/logging.py",
        "central/midcate.py",
        *concord_settings,
        *gears_settings,
        f"habitat/{_ENV}.py",
        optional("habitat/local.py") if _ENV != "production" else None,
    ),
)

# Include settings:
include(*_base_settings)
