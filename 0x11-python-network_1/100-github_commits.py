#!/usr/bin/python3
"""print 10 most recent commits"""
import requests
from sys import argv

if __name__ == "__main__":
    me = argv[2] + "/" + argv[1]
    url = "https://api.github.com/repos/" + me + "/commits"
    r = requests.get(url).json()
    try:
        for i in range(10):
            print(r[i].get('sha'), end=": ")
            print(r[i].get('commit').get('author').get('name'))
    except Exception:
        pass
