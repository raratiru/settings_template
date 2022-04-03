#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decouple import config


ADMINS = [
    (config("POET_ADMIN_NAME"), config("POET_ADMIN_EMAIL")),
]
MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = f"{config('POET_ADMIN_NAME')} <{config('POET_ADMIN_EMAIL')}>"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_SUBJECT_PREFIX = f"[Django] {config('POET_PROJECT')}"
