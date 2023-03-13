#!/usr/bin/node
console.log(typeof process.argv[2] && process.argv[3] === 'undefined' ? 'undefined' :process.argv[2] +' is '+ process.argv[3]);
