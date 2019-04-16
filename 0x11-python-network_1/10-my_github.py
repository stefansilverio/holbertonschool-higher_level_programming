#!/usr/bin/python3
# use github api to display ID
from requests.auth import HTTPBasicAuth
import requests
import sys
import pprint
if __name__ == "__main__":
    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    p = r.json()
    print(p.get('id'))
