#!/usr/bin/python3
"""Script fetches a URL, and gets a response"""
from urllib.request import urlopen, Request
from urllib.error import URLError
from sys import argv
from urllib.parse import urlencode


def display_post_header(url_str: str, email_arg: str):
    try:
        data = urlencode({"email": email_arg})
        email = data.encode("utf-8")
        req = Request(url_str, email)
        with urlopen(req) as response:
            output_body = response.read()
        print(output_body.decode("utf-8"))
    except URLError as e:
        if hasattr(e, "reason"):
            print(e.reason)
        elif hasattr(e, "code"):
            print(e.code)


if __name__ == "__main__":
    try:
        display_post_header(argv[1], argv[2])
    except IndexError:
        raise
