#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  while (x > 0) {
    theFunction('C is fun');
    --x;
  }
};
