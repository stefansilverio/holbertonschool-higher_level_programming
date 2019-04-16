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
    try:
        r = r.json()
        if len(r) > 0:
            print("{} {}".format([r.get('id')], r.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
