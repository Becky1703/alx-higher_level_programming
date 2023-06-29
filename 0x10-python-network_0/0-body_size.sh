#!/usr/bin/bash
#Takes in a URL, sends request to the URL and siplays size of the body in bytes
#+ using curl

curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
