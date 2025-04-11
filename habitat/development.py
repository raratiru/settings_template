#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from main.settings.central.base import DATABASES, INSTALLED_APPS
from main.settings.central.csp import CSP_IMG_SRC, CSP_SCRIPT_SRC
from main.settings.central.midcate import MIDDLEWARE

DEBUG = True

INSTALLED_APPS = INSTALLED_APPS + ("debug_toolbar",)
INTERNAL_IPS = ["127.0.0.1", "localhost"]  # Debug Toolbar
MIDDLEWARE = MIDDLEWARE + [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


def _custom_show_toolbar(request):
    """Only show the debug toolbar to users with the superuser flag."""
    user = getattr(request, "user", False)
    if user:
        return DEBUG and user.is_superuser
    else:
        return False


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": "main.settings.habitat.development._custom_show_toolbar",
}

# This will make debug toolbar to work with django-csp,
# since `ddt` loads some scripts from `ajax.googleapis.com`:
CSP_SCRIPT_SRC = CSP_SCRIPT_SRC + ("ajax.googleapis.com",)
CSP_IMG_SRC = CSP_IMG_SRC + ("data:",)

# Disable persistent DB connections
# https://docs.djangoproject.com/en/dev/ref/databases/#caveats
DATABASES["default"]["CONN_MAX_AGE"] = 0


# nplusone
# https://github.com/jmcarp/nplusone

# Should be the first in line:
# MIDDLEWARE = (  # noqa: WPS440
#     'nplusone.ext.django.NPlusOneMiddleware',
# ) + MIDDLEWARE

# Logging N+1 requests:
# NPLUSONE_RAISE = True  # comment out if you want to allow N+1 requests
# NPLUSONE_LOGGER = logging.getLogger('django')
# NPLUSONE_LOG_LEVEL = logging.WARN
# NPLUSONE_WHITELIST = [
#     {'model': 'admin.*'},
# ]

# django-test-migrations
# https://github.com/wemake-services/django-test-migrations

# Set of badly named migrations to ignore:
# DTM_IGNORED_MIGRATIONS = frozenset((
#     ('axes', '*'),
# ))
