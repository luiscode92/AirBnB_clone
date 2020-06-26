#!/usr/bin/python3
""" """

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """

    """

    intro = 'Hola como estas linda, en que te puedo ayudar?\n'
    prompt = '(hbnb) '

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

    def do_create(self, args):
        """
        Create a new instance of clas BaseModel and saves it to the JSON file
        """
        if not args:
            print('** class name missing **')
            return
        arg = args.split()
        try:
            new = eval(arg[0] + '()')
            print(new.id)
            new.save()
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
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 






    def do_destroy(self, args):
        """

        """
        classes = ['BaseModel']
        commands = args.split()
        lenght = len(commands)

        if args == "":
            print("** class name missing **")

        if commands[0] not in classes:
            print("** class doesn't exist **")
        
        if lenght == 1:
            print("** instance id missing **")

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
