#!/usr/bin/python3
# send POST request to server, display body of response
import requests
import sys
if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], email)
    print(r.text)
