#!/usr/bin/node

const argv = process.argv;

if (argv.length <= 3) {
  console.log('0');
} else {
  console.log();
  let max, secondMax;
  max = argv[2];
  for (let i = 3; i < argv.length; i++) {
    if (argv[i] > max) {
      secondMax = max;
      max = argv[i];
    }
  }
  console.log(secondMax);
}
