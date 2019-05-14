#!/usr/bin/node
// import array compute new array
const list = require('./100-data').list;
console.log(list);
let cnt = -1;
const newArray = list.map(function (num) {
  cnt++;
  return num * cnt;
});
console.log(newArray);
