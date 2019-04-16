#!/usr/bin/python3
# display value of header response variable
import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        html = res.info()
        print(html['X-Request-Id'])
