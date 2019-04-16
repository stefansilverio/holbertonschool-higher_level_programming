#!/usr/bin/python3
# send search request to Star Wars API
import requests
import sys
import pprint
if __name__ == "__main__":
    search = sys.argv[1]
    r = requests.get('https://swapi.co/api/people', {'search': search})
    p = r.json()
    print("Number of results: {}".format(p.get('count')))
    for i in p.get('results'):
        print(i.get('name'))
