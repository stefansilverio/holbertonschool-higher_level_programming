#!/usr/bin/node
/* print addition of two integers */

function add (a, b) {
  console.log(parseInt(a, 10) + parseInt(b, 10));
}

add(process.argv[2], process.argv[3]);
