#!/usr/bin/python3
# send request to URL and display body of response
import requests
import sys
if __name__ == "__main__":
        r = requests.get(sys.argv[1])
        e_code = r.status_code
        if e_code >= 400:
            print("Error code: {}".format(e_code))
        else:
            print(r.text)
