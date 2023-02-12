#!/usr/bin/env python3
# This script serializes instances to a JSON file
# it also deserializes JSON file to instances
import json
from models.base_model import BaseModel
from models.user import User

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
        try:
            with open(FileStorage.__file_path) as f:
                my_dict = json.load(f)
                for value in my_dict.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))                    
        except FileNotFoundError:
            pass
