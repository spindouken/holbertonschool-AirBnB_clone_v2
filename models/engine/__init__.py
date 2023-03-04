#!/usr/bin/python3
"""Module that creates a unique FileStorage instance for the application"""

import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
