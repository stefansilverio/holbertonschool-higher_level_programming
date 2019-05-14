#!/usr/bin/node
// print title of star wars movie
const request = require('request');

const options = {
  url: 'http://swapi.co/api/films/' + process.argv[2],
  method: 'GET',
  headers: {
    'Accept-Charset': 'utf-8',
    'User-Agent': 'Mozilla/5.0'
  }
};

request(options, function (err, res, body) {
  if (err) { console.log('Problem reaching URL: ', err); }

  let json = JSON.parse(body);
  console.log(json['title']);
});
