#!/usr/bin/python3
"""
Defines the Console class, serving as the project's entry point.
"""
from cmd import Cmd
from models import storage
from models.engine.error_file import *
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# Global variable of registered models
classes = storage.models


class HBNBCommand(Cmd):
    """Console-based driver for the AirBnb Clone.
    All interactions with the system are facilitated through this class.
    """

    prompt = "(hbnb) "

    def do_EOF(self, args):
        """Method that handles the EOF signal to exit the program."""
        return True

    def do_quit(self, args):
        """Method that handles the Quit command to exit the program"""
        return True

    def do_create(self, args):
        """Method with usage: create <class> <key 1>=<resultue 2> <key 2>=<resultue 2> ...
        Creates a new class instance with given keys/resultues and print its id.
        """
        args, length = strtok(args)

        if not length:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif length == 1:
            temp = eval(args[0])()
            print(temp.id)
            temp.save()
        else:
            print("** Too many argument for create **")
            pass

    def do_show(self, arg):
        """Method that shows an Instance of Model based on its ModelName and id eg.
        $ show MyModel instance_id
        Prints error message if either MyModel or instance_id is missing
        Prints an Error message for wrong MyModel or instance_id"""
        args, length = strtok(arg)

        if not length:
            print("** class name missing **")
        elif length == 1:
            print("** instance id missing **")
        elif length == 2:
            try:
                instance = storage.find_by_id(*args)
                print(instance)
            except NotFoundModelError:
                print("** class doesn't exist **")
            except NotFoundInstanceError:
                print("** no instance found **")
        else:
            print("** Too many argument for show **")
            pass

    def do_destroy(self, arg):
        """Method that deletes an Instance of Model base on its ModelName and id eg.
        $ destroy MyModel instance_id
        Print error message if either MyModel or instance_id is missing
        Print an Error message for wrong MyModel or instance_id"""
        args, length = strtok(arg)

        if not length:
            print("** class name missing **")
        elif length == 1:
            print("** instance id missing **")
        elif length == 2:
            try:
                storage.delete_by_id(*args)
            except NotFoundModelError:
                print("** class doesn't exist **")
            except NotFoundInstanceError:
                print("** no instance found **")
        else:
            print("** Too many argument for destroy **")
            pass

    def do_all(self, args):
        """ Method that retrieves all instances: eg.
        $ all
        $ all MyModel
        if MyModel is passed returns only instances of MyModel"""
        args, length = strtok(args)

        if length < 2:
            try:
                print(storage.find_all(*args))
            except NotFoundModelError:
                print("** class doesn't exist **")
        else:
            print("** Too many argument for all **")
            pass

    def do_update(self, arg):
        """Method that updates an instance based on its id eg
        $ update Model id missing_field resultue
        Throws errors for missing arguments"""
        args, length = strtok(arg)
        if not length:
            print("** class name missing **")
        elif length == 1:
            print("** instance id missing **")
        elif length == 2:
            print("** attribute name missing **")
        elif length == 3:
            print("** resultue missing **")
        else:
            try:
                storage.update_one(*args[0:4])
            except NotFoundModelError:
                print("** class doesn't exist **")
            except NotFoundInstanceError:
                print("** no instance found **")

    def do_models(self, arg):
        """Method that prints all registered Models"""
        print(*classes)

    def process_class_methods(self, arg):
        """Method that handles Class Methods
        <cls>.all(), <cls>.show() etc
        """

        method_patterns = ("all(", "show(", "count(", "create(")
        try:
            result = eval(arg)
            for i in method_patterns:
                if i in arg:
                    print(result)
                    break
            return
        except AttributeError:
            print("** inresultid method **")
        except NotFoundInstanceError:
            print("** no instance found **")
        except TypeError as er:
            missing_field = er.args[0].split()[-1].replace("_", " ")
            missing_field = missing_field.strip("'")
            print(f"** {missing_field} missing **")
        except Exception as e:
            print("** invalid syntax **")
            pass

    def default(self, arg):
        """Method that Overrides the default method to handle class methods"""
        if '.' in arg and arg.split('.')[0] in classes and arg[-1] == ')':
            return self.process_class_methods(arg)
        return Cmd.default(self, arg)

    def emptyline(self):
        """Method that Overrides empty line to do nothing"""
        return


    def strtok(line: str):
        """Function that splits a line by spaces"""
        args = shlex.split(line)
        return args, len(args)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
