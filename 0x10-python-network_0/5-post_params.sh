#!/bin/bash
#Sends a POST request to the passed URL and didplays the body of the response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
