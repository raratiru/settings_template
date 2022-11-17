#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

from decouple import config


# Languages

LANGUAGES = [("en", "English"), ("el", "Greek")]
LANGUAGE_CODE = "en"
LANGUAGE_COOKIE_NAME = f"{config('POET_PROJECT')}_language"
TIME_ZONE = "Europe/Athens"
USE_I18N = True
USE_THOUSAND_SEPARATOR = True
USE_TZ = True
LOCALE_PATHS = [
    Path(config("POET_PROJECT_DJANGO_PATH")) / "patois",
]

# Formats

DATE_FORMAT = "d-m-Y"
TIME_FORMAT = "H:i"
DATETIME_FORMAT = "d-m-Y H:i"
YEAR_MONTH_FORMAT = "F Y"
MONTH_DAY_FORMAT = "F j"
SHORT_DATE_FORMAT = "d/m/Y"
SHORT_DATETIME_FORMAT = "d/m/Y P"
FIRST_DAY_OF_WEEK = 1
DATE_INPUT_FORMATS = ("%d-%m-%Y",)  # '21-03-2014'
TIME_INPUT_FORMATS = (
    "%H:%M:%S",  # '17:59:59'
    "%H:%M",  # '17:59'
)
DATETIME_INPUT_FORMATS = ("%d-%m-%Y %H:%M",)  # '21-03-2014 17:59'

DECIMAL_SEPARATOR = ","
THOUSAND_SEPARATOR = "."
NUMBER_GROUPING = 3
