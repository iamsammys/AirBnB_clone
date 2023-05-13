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
        if not HBNBCommand.check_class(line):
            return
        cls = line[0]
        new_instance = eval(cls + "()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Show command to print string representation of instance
        """
        arg = args.split()
        if not HBNBCommand.check_class(arg):
            return
        if not HBNBCommand.check_id(arg):
            return
        key = "{}.{}".format(arg[0], arg[1])
        print(HBNBCommand.objects[key])

    def do_destroy(self, args):
        """deletes an instance based on class name and id
        """
        arg = args.split()
        if not HBNBCommand.check_class(arg):
            return
        if not HBNBCommand.check_id(arg):
            return
        key = "{}.{}".format(arg[0], arg[1])
        del HBNBCommand.objects[key]

    def check_class(args):
        """check if a class was passed and exists
        """
        if len(args) < 1:
            print("** class name missing **")
            return False
        cls = args[0]
        if cls not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        return True

    def check_id(arg):
        """checks that id was passed and id exists
        """
        if len(arg) < 2:
            print("** instance id missing **")
            return False
        id = arg[1]
        cls = arg[0]
        key = "{}.{}".format(cls, id)
        if key not in HBNBCommand.objects:
            print("** no instance found **")
            return False
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
