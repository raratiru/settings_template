#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sentry_sdk
from decouple import config
from sentry_sdk.integrations.django import DjangoIntegration


DEBUG = False

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 31536000
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_AGE = 43200
SESSION_COOKIE_SECURE = True

sentry_sdk.init(
    dsn=config("POET_SENTRY_URL"),
    integrations=[
        DjangoIntegration(),
    ],
)

# SECURE_REDIRECT_EXEMPT = [
#     # This is required for healthcheck to work:
#     '^health/',
# ]

# This is a hack to allow a special flag to be used with `--dry-run`
# to test things locally.
# _COLLECTSTATIC_DRYRUN = config(
#     'DJANGO_COLLECTSTATIC_DRYRUN', cast=bool, default=False,
# )
# Adding STATIC_ROOT to collect static files via 'collectstatic':
# STATIC_ROOT = '.static' if _COLLECTSTATIC_DRYRUN else '/var/www/django/static'
