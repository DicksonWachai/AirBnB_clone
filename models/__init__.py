#!/usr/bin/env python3
# This script creates a unique FileStorage instance
# of your application

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
