#!/usr/bin/python3
"""Script fetches a URL, and gets a response"""
from urllib.request import urlopen, Request
from urllib.error import URLError


def fetch_and_display():
    try:
        req = Request('https://alx-intranet.hbtn.io/status')
        with urlopen(req) as response:
            output_body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(output_body)))
            print("\t- content: {}".format(output_body))
            print("\t- utf8 content: {}".format(output_body.decode('utf-8')))
    except URLError as e:
        if hasattr(e, "reason"):
            print(e.reason)
        elif hasattr(e, "code"):
            print(e.code)


if __name__ == "__main__":
    fetch_and_display()
