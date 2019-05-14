#!/usr/bin/node
// return the number of occurences in a list
exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  let idx = 0;
  while (idx < list.length) {
    if (list[idx] === searchElement) { cnt++; }
    idx++;
  }
  return cnt;
};
