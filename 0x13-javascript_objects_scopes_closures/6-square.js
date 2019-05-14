#!/usr/bin/node
// define square that inherits from rectangle class
const Squar = require('./5-square');
module.exports = class Square extends Squar {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (typeof (c) === 'undefined') { c = 'X'; }
    let oIdx = 0;
    let iIdx = 0;
    let str = '';
    for (; this.height > oIdx; oIdx++) {
      str = '';
      for (; this.width > iIdx; iIdx++) { str += c; }
      iIdx = 0;
      console.log(str);
    }
  }
};
