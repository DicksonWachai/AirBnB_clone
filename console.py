#!/usr/bin/env python3
# This script is the console of the AirBnB clone

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {"BaseModel"}
    """Methods of the console"""
    def do_create(self, line):
        """Creation of new instances"""
        new_instance = parse(line)
        if len(new_instance) == 0:
            print("** class name missing **")
        elif new_instance[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(new_instance[0])().id)
            storage.save()

    def do_show(self, line):
        """String representation of an instance"""
        args = parse(line)
        my_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in my_dict:
            print("** no instance found **")
        else:
            print(my_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, line):
        """Deletes an instance"""
        args = parse(line)
        my_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in my_dict:
            print("** no instance found **")
        else:
            del my_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_EOF(self, line):
        """Ënds the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Does nothing"""
        pass

def parse(args):
    return args.split()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
