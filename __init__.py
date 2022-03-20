#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from split_settings.tools import optional, include


include(
    "central/01_default_settings.py",
    "central/02_base_settings.py",
    optional("habitat/10_rehearsals.py"),
)
