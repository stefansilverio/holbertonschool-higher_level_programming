#!/usr/bin/node
/* computes and prints a factorial */
function fact (num) {
  if (num === 0) { return 1; } else { return (num * fact(num - 1)); }
}

let num = 0;
if (isNaN(process.argv[2]) === true || process.argv.length < 3) { console.log(1); } else {
  num = Number(process.argv[2]);
  console.log(fact(num));
}
