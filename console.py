#!/usr/bin/python3
"""Module for command line interpreter for models
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter
    """
    prompt = "(hbnb)"
    classes = [
            "BaseModel",
            ]
    objects = storage.all()

    def do_EOF(self, line):
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the CLI
        """
        return True

    def do_emptyline():
        """method to do nothing when an empty line is inputed
        """
        pass
    
    def do_create(self, lines):
        """Create command to create a new instance of a class
        """
        line = lines.split()
        if len(line) < 1:
            print("** class name missing **")
            return
        cls = line[0]
        if cls not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(cls + "()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Show command to print string representation of instance
        """
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
            return
        cls = arg[0]
        if cls not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        id = arg[1]
        key = "{}.{}".format(cls, id)
        if key not in HBNBCommand.objects:
            print("** no instance found **")
            return
        print(HBNBCommand.objects[key])

if __name__ == "__main__":
    HBNBCommand().cmdloop()
