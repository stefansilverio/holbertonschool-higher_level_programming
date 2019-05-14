#!/usr/bin/node
// display status code of get request
const request = require('request');

request(process.argv[2])
  .on('response', function (response) {
    console.log('code: ' + response.statusCode);
  })

  .on('error', function (err) {
    console.log('Problem reaching URL: ', err);
  });
