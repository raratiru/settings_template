#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://sobolevn.me/2020/03/do-not-log
https://github.com/hynek/structlog
"""

from pathlib import Path

from decouple import config


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "{levelname} {asctime} {process:d} {thread:d} {name} {lineno} {message}"
            ),
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {name} {lineno} {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "logging.FileHandler",
            "filename": Path(config("POET_PROJECT_PATH"))
            / "www"
            / "logs"
            / "django.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": True,
        },
        "django": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
