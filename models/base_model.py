#!/usr/bin/env python3
# This Script defines a BaseModel clas with
# all common attributes for other classes

import uuid
from datetime import datetime


class BaseModel:
    """All attributes and methods"""
    def __init__(self, *args, **kwargs):
        """"Defines the public
        instance attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k in ["created_at", "updated_at"]:
                        v = datetime.\
                                strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)

    def __str__(self):
        """A string representation of an object"""
        return (f"[{self.__class__.__name__}] <{self.id}> {self.__dict__}")

    def save(self):
        """updates instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__
        my_dict.update({
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat()
            })
        return my_dict
