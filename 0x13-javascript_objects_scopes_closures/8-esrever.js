#!/usr/bin/node
// returns reversed versions of a list
exports.esrever = function (list) {
  let cp = [];
  let rev = list.length - 1;
  let idx = 0;
  while (list.length > idx) {
    cp[idx] = list[rev];
    idx++;
    rev--;
  }
  return cp;
};
