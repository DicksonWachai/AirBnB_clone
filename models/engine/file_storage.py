#!/usr/bin/env python3
# This script serializes instances to a JSON file
# it also deserializes JSON file to instances
import json
from models.base_model import BaseModel

class FileStorage:
    """All methods and attributes of this class"""
    # Private class attributes
    __file_path = "file.json"
    __objects = {}

    # Public instance methods
    def all(self):
        """Returns dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes dictionary to JSON file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes JSON file into instances"""
        my_dict = {"BaseModel": BaseModel}
        obj = {}
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_data = json.load(f)
                for key, value in json_data.items():
                    obj[key] = my_dict[value["__class__"]](**value)
                FileStorage.__objects = obj
        except FileNotFoundError:
            pass
