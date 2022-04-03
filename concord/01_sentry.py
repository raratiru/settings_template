#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sentry_sdk
from decouple import config


sentry_login = config("POET_SENTRY_URL", default=None)

if sentry_login:
    sentry_sdk.init(
        dsn=sentry_login,
        integrations=[
            sentry_sdk.integrations.DjangoIntegration(),
        ],
    )
