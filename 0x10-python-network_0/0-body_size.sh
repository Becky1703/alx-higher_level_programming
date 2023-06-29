#!/usr/bin/bash
#Takes in a URL, sends request to the URL and siplays size of the body in bytes
#+ using curl, and testing on a server running on port 5000

curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
