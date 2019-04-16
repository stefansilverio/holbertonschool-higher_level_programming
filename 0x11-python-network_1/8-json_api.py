#!/usr/bin/python3
# send letter as parameter to server as POST request
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        q = ""
    else:
        q = sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", {'q': q})
    if len(r.json()) > 0 and type(r.json()) is dict:
        r = r.json()
        print("{} {}".format([r.get('id')], r.get('name')))
    elif type(r.json()) is not dict:
        print("Not a valid JSON")
    else:
        print("No result")
