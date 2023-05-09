#!/usr/bin/python3
"""module to serialise and deserialise objs
to and from filestorage respectively
created by:
    Samuel Ezeh
    Emmanuel Ochoja
"""


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

    def new(self):
        """sets in __objects the obj with key
        """
        key = "{}.{}".format(self.__class__.__name__, self.id)
        FileStorage.__objects[key] = self

    def save(self):
        """serializes __objects to the JSON file
        """
        new_dict = {}
        file_name = FileStorage.__file_path
        objects = FileStorage.__objects
        for key, value in objects.items():
            new_dict[key] = value.to_dict()
        with open(file_name, "w") as file:
            json.dump(file, new_dict)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        file_name = FileStorage.__file_path
        try:
            with open(file_name, "r") as file:

