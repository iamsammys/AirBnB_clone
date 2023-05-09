#!/usr/bin/python3
"""The base model of the AirBnB web app

created by:
    Samuel Ezeh
    Emmanuel Ochoja
"""

from datetime import datetime
import uuid


class BaseModel:
    """the base class of the project
    """
    def __init__(self, *args, **kwargs):
        """initialises the class instances
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def __str__(self):
        """returns the string representation of the object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns the dictionary representation of the object

        Return:
            dictionary of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = __class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
