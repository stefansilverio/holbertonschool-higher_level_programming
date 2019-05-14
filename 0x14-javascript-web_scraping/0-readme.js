#!/usr/bin/node
// read and print content of file
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) { console.log(err); } else { process.stdout.write(data.toString()); }
});
