#!/usr/bin/node
// convert # to another base
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
