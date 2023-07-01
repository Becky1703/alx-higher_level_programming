#!/usr/bin/python3
"""Script fetches a URL, and gets a response"""
from urllib.request import urlopen, Request
from urllib.error import URLError
from sys import argv


def display_header_value(url_str: str):
    try:
        req = Request(url_str)
        with urlopen(req) as response:
            output_body = response.read()
        print(response.info().get("X-Request-Id"))
    except URLError as e:
        if hasattr(e, "reason"):
            print(e.reason)
        elif hasattr(e, "code"):
            print(e.code)


if __name__ == "__main__":
    display_header_value(argv[1])
