#!/usr/bin/node
/* define a rectangle */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else { constructor(); }
  }
  print () {
    let oIdx = 0;
    let iIdx = 0;
    let str = '';
    for (; this.height > oIdx; oIdx++) {
      str = '';
      for (; this.width > iIdx; iIdx++) { str += 'X'; }
      iIdx = 0;
      console.log(str);
    }
  }
};
