# -*- coding: utf-8 -*-
"""The database CRUD module, including the CRUD and user auth."""
from flask import Blueprint
db_crud = Blueprint('db_crud',__name__,static_folder="../static")

from . import views  # noqa
