#!/usr/bin/node
// print number of movies w/ character
const request = require('request');

const options = {
  url: 'http://swapi.co/api/films',
  method: 'GET',
  headers: {
    'Accept-Charset': 'utf-8',
    'User-Agent': 'Mozilla/5.0'
  }
};

request(options, function (err, res, body) {
  if (err) { console.log(err); }

  let cnt = 0;
  let idx = 0;
  let json = JSON.parse(body);
  let test = '18';
  for (; idx < json['results'].length; idx++) {
    let str = json['results'][idx]['characters'] + ',';
    if (str.indexOf(test) >= 0) { cnt++; }
  }
  console.log(cnt);
});
