#!/usr/bin/node
/* print 2nd largest number in list */
let result = process.argv.map(Number);
result = result.slice(2);
let SecondMax = 0;
let Max = 0;
let idx;

for (idx = 0; idx < result.length; idx++) {
  if (result[idx] >= Max) {
    SecondMax = Max;
    Max = result[idx];
  } else {
    if (result[idx] > SecondMax) { SecondMax = result[idx]; }
  }
}
console.log(SecondMax);
