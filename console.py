#!/usr/bin/python3
""" """

import cmd
import string
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """

    """

    intro = 'Hola como estas linda, en que te puedo ayudar?\n'
    prompt = '(hbnb) '

    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
               "Review"]

    def emptyline(self):
        """
        Method to handle an empy line
        """

        pass

    def do_quit(self, args):
        """
        Quit command to exit the progra
        """

        return True

    def do_EOF(self, args):
        """
        Quit command to exit the program
        """

        return True

    def default(self, args):
        commands = args.split('.')
        try:
            if commands[1] == 'all()':
                self.do_all(commands[0])
            elif commands[1] == 'count()':
                self.count(commands[0])
            elif 'show(' in commands[1]:
                params = commands[1].split('(')
                self.do_show(commands[0] + ' ' + params[1].split('"')[1])
            elif 'destroy(' in commands[1]:
                params = commands[1].split('(')
                self.do_destroy(commands[0] + ' ' + params[1].split('"')[1])
        except:
            pass

    def do_create(self, args):
        """
        Create a new instance of clas BaseModel and saves it to the JSON file
        """
        if not args:
            print('** class name missing **')
            return
        arg = args.split()
        try:
            new = eval(arg[0])
            model = new()
            print(model.id)
            model.save()
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Print and instance based on the class name and id
        """

        if not args:
            print('** class name missing **')
            return

        arg = args.split()

        if arg[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                if key == "{}.{}".format(arg[0], arg[1]):
                    print(value)
                    return
            print('** no instance found **')

    def do_destroy(self, args):
        """

        """

        commands = args.split()
        lenght = len(commands)

        if args == "":
            print("** class name missing **")
            return
        elif commands[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif lenght == 1:
            print("** instance id missing **")
            return
        else:
            obj_dict = storage.all()
            for key, value in obj_dict.items():
                if "{}.{}".format(commands[0], commands[1]) == key:
                    del obj_dict[key]
                    storage.save()
                    return
        print("** no instance found **")

    def do_all(self, args):
        """

        """

        commands = args.split()
        lenght = len(commands)
        obj_list = []
        obj_dict = storage.all()

        if lenght == 0:
            for key, value in obj_dict.items():
                obj_list.append(str(value))
            print(obj_list)

        elif commands[0] in HBNBCommand.classes:
            for key, value in obj_dict.items():
                if commands[0] in key:
                    obj_list.append(str(value))
            print(obj_list)

        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        """

        commands = args.split()
        lenght = len(commands)
        flag = 1

        if args == "":
            print("** class name missing **")
            return
        elif commands[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif lenght == 1:
            print("** instance id missing **")
            return
        else:
            for key, value in storage.all().items():
                if "{}.{}".format(commands[0], commands[1]) == key:
                    flag = 0
        if flag:
            print("** no instance found **")
            return
        elif lenght == 2:
            print("** attribute name missing **")
            return
        elif lenght == 3:
            print("** value missing **")
            return
        else:
            for key, value in storage.all().items():
                if "{}.{}".format(commands[0], commands[1]) == key:
                    if checkInt(commands[3]):
                        setattr(value, commands[2],
                                int(commands[3].strip('"')))
                    elif checkFloat(commands[3]):
                        setattr(value, commands[2],
                                float(commands[3].strip('"')))
                    else:
                        setattr(value, commands[2], commands[3].strip('"'))
        storage.save()

    @staticmethod
    def count(class_name):
        """
        """

        counter = 0

        if class_name in HBNBCommand.classes:
            for key, value in storage.all().items():
                if class_name in key:
                    counter += 1
        print(counter)


def checkInt(command):
    """
    Checks if a string is an Integer
    """

    try:
        int(command.strip('"'))
        return 1
    except:
        return 0


def checkFloat(command):
    """
    Checks if a string is a Float
    """

    try:
        float(command.strip('"'))
        return 1
    except:
        return 0


if __name__ == '__main__':
    HBNBCommand().cmdloop()
