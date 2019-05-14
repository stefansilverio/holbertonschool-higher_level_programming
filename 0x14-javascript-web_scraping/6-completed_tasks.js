#!/usr/bin/node
// compute number of tasks completed
const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET',
  headers: {
    'Accept-Charset': 'utf-8',
    'User-Agent': 'Mozilla/5.0'
  }
};

request(options, function (err, res, body) {
  let json = JSON.parse(body);
  let dict = {};
  if (err) { console.log(err); } else {
    json.forEach((user) => {
      let id = user.userId.toString();
      if (!dict[id]) { dict[id] = 0; }

      if (user.completed === true) {
        dict[id] += 1;
      }
    });
    console.log(dict);
  }
});
