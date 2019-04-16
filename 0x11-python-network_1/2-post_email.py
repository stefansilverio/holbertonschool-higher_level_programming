#!/usr/bin/python3
# send POST request to URL and display body
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(values)
    email = email.encode('ascii')
    req = urllib.request.Request(sys.argv[1], email)
    with urllib.request.urlopen(req) as res:
        html = res.read()
        print("{}".format(html.decode('utf-8')))
