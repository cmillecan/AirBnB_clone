#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
import models
from models import storage

modelnames = ("BaseModel", "")

class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = '(hbnb) '

    def do_create(self, line):
        items = line.split()
        if len(items) is 0:
            print("** class name missing **")
            return
        if (items[0] in modelnames):
            #do the create Model and print id
            model = eval(items[0] + "()")
            storage.new(model)
            storage.save()
            print(model.id)
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        vals = list(storage.all().values())
        if line == "BaseModel":
            print([str(val) for val in vals])
        else:
            print("** class doesn't exist **")

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """
        Do none
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
