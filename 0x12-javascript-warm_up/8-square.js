#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const y = Number(process.argv[2]);
  let i = 0;
  while (i < y) {
    console.log('X'.repeat(y));
    i++;
  }
}
