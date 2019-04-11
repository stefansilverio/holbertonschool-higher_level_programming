#!/bin/bash
# display all HTTP methods
curl -si -X OPTIONS $1 | grep '^\Allow:' | cut -d ':' -f 2 | sed -e 's/^[ \t]*//'
