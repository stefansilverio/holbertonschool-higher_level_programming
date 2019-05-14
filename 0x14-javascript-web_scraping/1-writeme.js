#!/usr/bin/node
// write a string to a file
const fs = require('fs');
let data = process.argv[3];
fs.writeFile(process.argv[2], data, 'utf8', (err) => {
  if (err) { console.log(err); }
});
