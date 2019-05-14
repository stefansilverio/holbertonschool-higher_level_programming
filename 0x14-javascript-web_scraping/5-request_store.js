#!/usr/bin/node
// store contents of webpage in file
const request = require('request');
const fs = require('fs');

request
  .get(process.argv[2])
  .on('error', function(err) {
    console.error(err)
  })
  .pipe(fs.createWriteStream(process.argv[3]))
