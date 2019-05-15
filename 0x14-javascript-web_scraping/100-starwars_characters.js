#!/usr/bin/node
// prints all characters of Star Wars movie
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
  let json = JSON.parse(body);
  if (err) { console.log(err); } else {
    json['characters'].forEach(function (element) {
      request.get(element, function (err, res, body) {
        let jso = JSON.parse(body);
        if (err) { console.log(err); } else { console.log(jso['name']); }
      });
    });
  }
});
