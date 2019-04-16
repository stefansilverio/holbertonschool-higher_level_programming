#!/usr/bin/python3
# send search request to Star Wars API
import requests
import sys
if __name__ == "__main__":
    search = sys.argv[1]
    search = {'search': search}
    r = requests.get('https://swapi.co/api/people', params=search)
    p = r.json()
    print("Number of results: {}".format(p.get('count')))
    for i in p.get('results'):
        print(i.get('name'))
