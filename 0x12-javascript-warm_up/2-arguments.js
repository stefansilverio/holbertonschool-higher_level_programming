#!/usr/bin/node
/* print message depending on number of args */
let size = process.argv.length;
if (size === 2) { console.log('No argument'); } else if (size === 3) { console.log('Argument found'); } else { console.log('Arguments found'); }
