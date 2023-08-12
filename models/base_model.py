#!/usr/bin/python3

"""
A class BaseModel that defines all common attributes/methods for other classes.
"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """The base model class for all objects."""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in {"created_at", "updated_at"}:
                    setattr(
                        self,
                        key,
                        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        )
                elif key == "__class__":
                    setattr(self, key, type(self))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            now = datetime.now()
            self.created_at = now
            self.updated_at = now
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A formatted string containing class name, ID,
                 and attribute dictionary.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute and saves the BaseModel instance.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary representation.

        Returns:
            dict: A dictionary containing instance attributes.
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = type(self).__name__
        instance_dict["created_at"] = instance_dict["created_at"].isoformat()
        instance_dict["updated_at"] = instance_dict["updated_at"].isoformat()
        return instance_dict
