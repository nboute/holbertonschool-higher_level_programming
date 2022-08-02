#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let line = [];
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      line += c;
    }
    for (let i = 0; i < this.size; i++) {
      console.log(line);
    }
  }
};
