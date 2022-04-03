#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..central.midcate import MIDDLEWARE
from ..central.base import DATABASES


DEBUG = True

INTERNAL_IPS = ["127.0.0.1", "localhost"]  # Debug Toolbar
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
] + MIDDLEWARE


def _custom_show_toolbar(request):
    """Only show the debug toolbar to users with the superuser flag."""
    return DEBUG and request.user.is_superuser


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": "server.settings.environments.development._custom_show_toolbar",
}

# This will make debug toolbar to work with django-csp,
# since `ddt` loads some scripts from `ajax.googleapis.com`:
CSP_SCRIPT_SRC = ("'self'", "ajax.googleapis.com")
CSP_IMG_SRC = ("'self'", "data:")
CSP_CONNECT_SRC = ("'self'",)

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
