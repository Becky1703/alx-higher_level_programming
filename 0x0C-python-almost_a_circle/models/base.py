#!/usr/bin/python3
"""Base Class"""
import json
import csv
import turtle


class Base:
    """Base class that defines the base for all other classes.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string representation of

        list_dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string representatio

        of list_objs to a file.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """REturns an instance of all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except I0Error:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serialization in csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as a_csvfile:
            if list_objs is None or list_objs == []:
                a_csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(a_csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of classes instantiated from CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as a_csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(a_csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangle and Square using turtle module"""
        t = turtle.Turtle()
        t.screen.bgcolor("#a52826")
        t.pensize(4)
        t.shape("turtle")

        t.color("#C0C0C0")
        for rect in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(rect.x, rect.y)
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.hideturtle()

        t.color("#bb2e2d")
        for sq in list_squares:
            t.showturtle()
            t.up()
            t.goto(sq.x, sq.y)
            t.down()
            for i in range(2):
                t.forward(sq.width)
                t.left(90)
                t.forward(sq.height)
                t.left(90)
            t.hideturtle()

        turtle.exitonclick()
