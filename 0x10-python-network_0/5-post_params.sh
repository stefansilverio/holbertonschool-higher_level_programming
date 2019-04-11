#!/bin/bash
# send POST request to URL
curl -Ls $1 -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
