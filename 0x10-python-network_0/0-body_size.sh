#!/bin/bash
#Takes in a URL, sends request to the URL and displays size of the body in bytes
curl -s "$1" | wc -c
