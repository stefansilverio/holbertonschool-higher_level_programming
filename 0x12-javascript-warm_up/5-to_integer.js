#!/usr/bin/node
/* convert arg to integer */
if (isNaN(process.argv[2]) === true)
  console.log('Not a number');
else
{
  let num = parseInt(process.argv[2], 10)
  console.log('My number: ' + num);
}
