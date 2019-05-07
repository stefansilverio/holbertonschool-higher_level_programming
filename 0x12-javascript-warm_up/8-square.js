#!/usr/bin/node
/* print a square */
let Iidx, Oidx;
if (isNaN(process.argv[2]) === true) { console.log('Missing size'); } else {
  for (Oidx = 0; Oidx < process.argv[2]; Oidx++) {
    let str = '';
    for (Iidx = 0; Iidx < process.argv[2]; Iidx++) { str += 'X'; }
    console.log(str);
  }
}
