#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from main.settings.central.base import DATABASES


CORS_ALLOW_ALL_ORIGINS = True
DEBUG = True

INTERNAL_IPS = ["127.0.0.1", "localhost"]  # Debug Toolbar

# Disable persistent DB connections
# https://docs.djangoproject.com/en/dev/ref/databases/#caveats
DATABASES["default"]["CONN_MAX_AGE"] = 0
