#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('undefined', 'is', 'undefined');
} else if (process.argv.length === 4) {
  console.log(process.argv[2], 'is', process.argv[3]);
} else {
  console.log(process.argv[2], 'is', 'undefined');
}
