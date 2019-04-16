#!/usr/bin/python3
# send request to URL & display body of response
import urllib.request
import sys
if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            result = res.read()
            print(result.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
