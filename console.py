#!/usr/bin/python3
"""HBnB console."""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse_arg(arg):
    curly_brac = re.search(r"\{(.*?)\}", arg)
    brac = re.search(r"\[(.*?)\]", arg)
    if curly_brac is None:
        if brac is None:
            return [x.strip(",") for x in split(arg)]
        else:
            lex = split(arg[:brac.span()[0]])
            rel = [x.strip(",") for x in lex]
            rel.append(brac.group())
            return rel
    else:
        lex = split(arg[:curly_brac.span()[0]])
        rel = [x.strip(",") for x in lex]
        rel.append(curly_brac.group())
        return rel


class HBNBCommand(cmd.Cmd):
    """Command interpreter.

    Classattributes:
        prompt (string): The command prompt.
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

    def empty_line(self):
        """Do nothing ."""
        pass

    def default(self, arg):
        """Default behavior for cmd """
        ardict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        mat = re.search(r"\.", arg)
        if mat is not None:
            arl = [arg[:mat.span()[0]], arg[mat.span()[1]:]]
            mat = re.search(r"\((.*?)\)", arl[1])
            if mat is not None:
                comd = [arl[1][:mat.span()[0]], mat.group()[1:-1]]
                if comd[0] in ardict.keys():
                    call = "{} {}".format(arl[0], comd[1])
                    return ardict[comd[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit."""
        return True

    def do_EOF(self, arg):
        """EOF."""
        print("")
        return True

    def do_create(self, arg):
        """usage: create <class>  """
        arl = parse_arg(arg)
        if len(arl) == 0:
            print("** class name missing **")
        elif arl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arl[0])().id)
            storage.save()

    def do_show(self, arg):
        """This displays the string representation
        of a class instance of a given id.
        """
        arl = parse_arg(arg)
        obdict = storage.all()
        if len(arl) == 0:
            print("** class name missing **")
        elif arl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arl[0], arl[1]) not in obdict:
            print("** no instance found **")
        else:
            print(obdict["{}.{}".format(arl[0], arl[1])])

    def do_destroy(self, arg):
        """This deletes a class instance of a given id."""
        arl = parse_arg(arg)
        obdict = storage.all()
        if len(arl) == 0:
            print("** class name missing **")
        elif arl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arl[0], arl[1]) not in obdict.keys():
            print("** no instance found **")
        else:
            del obdict["{}.{}".format(arl[0], arl[1])]
            storage.save()

    def do_all(self, arg):
        """This displays string representations
        of all instances of a given class.
        """
        arl = parse_arg(arg)
        if len(arl) > 0 and arl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            ob = []
            for oj in storage.all().values():
                if len(arl) > 0 and arl[0] == oj.__class__.__name__:
                    ob.append(oj.__str__())
                elif len(arl) == 0:
                    ob.append(oj.__str__())
            print(ob)

    def do_count(self, arg):
        """This retrieves the number of instances of a given class."""
        arl = parse_arg(arg)
        cnt = 0
        for ob in storage.all().values():
            if arl[0] == ob.__class__.__name__:
                cnt += 1
        print(cnt)

    def do_update(self, arg):
        """This updates a class instance of a given id."""
        arl = parse_arg(arg)
        obdict = storage.all()

        if len(arl) == 0:
            print("** class name missing **")
            return False
        if arl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arl[0], arl[1]) not in obdict.keys():
            print("** no instance found **")
            return False
        if len(arl) == 2:
            print("** attribute name missing **")
            return False
        if len(arl) == 3:
            try:
                type(eval(arl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arl) == 4:
            ob = obdict["{}.{}".format(arl[0], arl[1])]
            if arl[2] in ob.__class__.__dict__.keys():
                valuetype = type(ob.__class__.__dict__[arl[2]])
                oj.__dict__[arl[2]] = valuetype(arl[3])
            else:
                ob.__dict__[arl[2]] = arl[3]
        elif type(eval(arl[2])) == dict:
            ob = obdict["{}.{}".format(arl[0], arl[1])]
            for x, y in eval(arl[2]).items():
                if (x in ob.__class__.__dict__.keys() and
                        type(ob.__class__.__dict__[x]) in {str, int, float}):
                    valuetype = type(ob.__class__.__dict__[x])
                    ob.__dict__[x] = valuetype(y)
                else:
                    ob.__dict__[x] = y
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
