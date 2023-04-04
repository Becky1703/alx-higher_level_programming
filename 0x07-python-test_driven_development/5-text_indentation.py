#!/usr/bin/python3
"""A function that prints a text with two new lines"""


def text_indentation(text):
    """
    




    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    new_text = ""


    for i in range(len(text)):
        if text[i] in chars:
            new_text += text[i] + "\n\n"
        else:
            new_text += text[i]


    lines = new_text.split("\n")


    for line in lines:
        print(line.strip())
