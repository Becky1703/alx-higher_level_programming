#!/usr/bin/python3
"""Function tat reads a text"""


def read_file(filename=""):
    with open("my_file_0.txt", encoding="utf-8") as f:
        print(f.read(), end="")
