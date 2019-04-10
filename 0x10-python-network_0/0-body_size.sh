#!/bin/bash
# send GET request to url - display response
curl -s "$1" | wc -c
