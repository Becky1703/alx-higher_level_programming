#!/usr/bin/bash
#Takes in a URL, sends request to the URL and displays size of the body in bytes
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
