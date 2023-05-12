#!/usr/bin/python3
"""module to serialise and deserialise objs
to and from filestorage respectively
created by:
    Samuel Ezeh
    Emmanuel Ochoja
"""

from models.base_model import BaseModel
import json


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
                for key, value in new_dict.items():
                    obj = BaseModel(**value)
                    self.new(obj)
        except Exception:
            print("reload was not successful")
