#!/usr/bin/env python3
# This script is the console of the AirBnB clone

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            }
    """Methods of the console"""
    def emptyline(self):
        """Does Nothing"""
        pass

    def do_create(self, line):
        """"Creates a new instance"""
        args = parse(line)
        my_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, line):
        """ Prints the string representation of an instance based on:
        the class name and id
        """
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
        """Deletes an instance based on the class name and id"""
        args = parse(line)
        my_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in my_dict.keys():
            print("** no instance found **")
        else:
            del my_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name
        """
        args = parse(line)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj1 = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj1.append(obj.__str__())
                elif len(args) == 0:
                    obj1.append(obj.__str__())
            print(obj1)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_EOF(self, line):
        """Signal to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        print()
        return True


def parse(args):
    return args.split()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
