#!/usr/bin/python3
"""creates a unique FileStorage
instance for your application
created by:
    Samuel Ezeh
    Emmanuel Ochoja
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
