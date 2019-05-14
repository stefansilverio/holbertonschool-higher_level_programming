#!/usr/bin/node
// print the argument and number of args printed
var cnt = 0;
exports.logMe = function (item) {
  console.log(cnt + ': ' + item);
  cnt++;
};
