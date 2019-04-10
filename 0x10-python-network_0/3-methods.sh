#!/bin/bash
# send DELETE request to URL
curl -si -X OPTIONS $1 | grep -o "OPTIONS, HEAD, PUT"
