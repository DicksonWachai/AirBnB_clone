#!/usr/bin/env python3
# This script is the console of the AirBnB clone

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    """Methods of the console"""
    def do_EOF(self, line):
        """Ënds the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
