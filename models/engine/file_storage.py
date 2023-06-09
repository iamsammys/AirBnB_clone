#!/usr/bin/python3
"""module to serialise and deserialise objs
to and from filestorage respectively
created by:
    Samuel Ezeh
    Emmanuel Ochoja
"""

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json

classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        }


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """returns the dictionary __objects

        Returns:
            the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
        """
        new_dict = {}
        file_name = FileStorage.__file_path
        objects = self.all()
        for key, value in objects.items():
            new_dict[key] = value.to_dict()
        with open(file_name, "w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        file_name = FileStorage.__file_path
        try:
            with open(file_name, "r") as file:
                new_dict = json.load(file)
                for key in new_dict:
                    cls = classes[new_dict[key]["__class__"]]
                    obj = cls(**new_dict[key])
                    self.new(obj)
        except Exception as error:
            pass
