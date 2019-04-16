#!/usr/bin/python3
# fetch a URL
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        html = res.read()
    print("Body response:")
    print("    - type: {}".format(type(html)))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(html.decode('utf-8')))
