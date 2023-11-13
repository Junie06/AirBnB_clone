#!/usr/bin/python3
"""
Initialization dunder method for the 'models' directory.
"""
from models.engine.file_storage import FileStorage

# Initialize a FileStorage instance for data storage.
storage = FileStorage()

# Reload data from storage to populate the program's models.
storage.reload()
