#!/usr/bin/python3
"""Script fetches a URL, and gets a response"""
import requests
from sys import argv


def header_value(url: str):
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))


if __name__ == "__main__":
    header_value(argv[1])
