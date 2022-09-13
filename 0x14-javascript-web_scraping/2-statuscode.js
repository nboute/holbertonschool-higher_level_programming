#!/usr/bin/node

const axios = require('axios');
const argv = process.argv;

axios
  .get(argv[2])
  .then(res => {
    console.log(`code: ${res.status}`);
  })
  .catch(error => {
    console.log(`code: ${error.response.status}`);
  });
