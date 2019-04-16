#!/usr/bin/python3
# display value of variable in response header
import requests
import sys
r = requests.get(sys.argv[1])
print(r.headers['X-Request-Id'])
