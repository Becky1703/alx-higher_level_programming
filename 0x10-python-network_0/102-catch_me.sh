#!/bin/bash
#Makes a request to 0.0.0.0:5000/catch_me that cause that the server to respond with with a message
curl -s -o /dev/null -w "You got me!" 0.0.0.0:5000/catch_me
