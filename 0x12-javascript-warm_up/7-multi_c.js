#!/usr/bin/node
/* prints text 'x' times */
let idx;
if (isNaN(process.argv[2]) === true) { console.log('Missing number of occurrences'); }
for (idx = 0; idx < process.argv[2]; idx++) { console.log('C is fun'); }
