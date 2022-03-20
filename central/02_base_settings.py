#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decouple import config
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = config("SECRET_KEY")
