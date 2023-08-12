#!/usr/bin/python3

"""A program called console.py that contains the entry point of
the command interpreter."""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """
    Parse the given argument into a list of tokens.

    Args:
        arg (str): The argument to be parsed.

    Returns:
        list: List of tokens extracted from the argument.
    """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    Interactive command-line interface for managing HBNB objects.

    Attributes:
        prompt (str): The command prompt shown to the user.
        __classes (set): Set of available class names.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
        }

    def emptyline(self):
        """Override the default behavior for empty lines."""
        pass

    def default(self, arg):
        """
        Handle unknown commands with this method.

        Args:
            arg (str): The command argument.

        Returns:
            bool: False if the command was not recognized.
        """
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(arg_list[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """
        Exit the command-line interface.

        Args:
            arg (str): The command argument.

        Returns:
            bool: True to exit the interface.
        """
        return True

    def do_EOF(self, arg):
        """
        Handle the End-of-File signal.

        Args:
            arg (str): The command argument.

        Returns:
            bool: True to exit the interface.
        """
        print("")
        return True

    def do_create(self, arg):
        """
        Create a new instance of a specified class.

        Args:
            arg (str): The class name.

        Returns:
            None
        """
        arg_list = parse(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Display information about a specific instance.

        Args:
            arg (str): The class name and instance ID.

        Returns:
            None
        """
        arg_list = parse(arg)
        objdict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, arg):
        """
        Delete a specific instance.

        Args:
            arg (str): The class name and instance ID.

        Returns:
            None
        """
        arg_list = parse(arg)
        objdict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()

    def do_all(self, arg):
        """
        Display information about all instances or instances of
        a specific class.

        Args:
            arg (str): The optional class name.

        Returns:
            None
        """
        arg_list = parse(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = [
                obj.__str__()
                for obj in storage.all().values()
                if len(arg_list) == 0 or arg_list[0] == obj.__class__.__name__
                ]
            print(objl)

    def do_count(self, arg):
        """
        Count the number of instances of a specific class.

        Args:
            arg (str): The class name.

        Returns:
            None
        """
        arg_list = parse(arg)
        count = sum(
            1 for obj in storage.all().values()
            if arg_list[0] == obj.__class__.__name__
            )
        print(count)

    def do_update(self, arg):
        """
        Update attributes of a specific instance.

        Args:
            arg (str): The class name, instance ID, attribute name, and value.

        Returns:
            None
        """
        arg_list = parse(arg)
        objdict = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_list) == 4:
            obj = objdict["{}.{}".format(arg_list[0], arg_list[1])]
            if arg_list[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_list[2]])
                obj.__dict__[arg_list[2]] = valtype(arg_list[3])
            else:
                obj.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            obj = objdict["{}.{}".format(arg_list[0], arg_list[1])]
            for k, v in eval(arg_list[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
