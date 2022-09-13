#!/usr/bin/node

const axios = require('axios');
const argv = process.argv;

axios
  .get(`https://swapi-api.hbtn.io/api/films/${argv[2]}`)
  .then(res => {
    res.data.characters.forEach(function (url) {
      axios
        .get(url)
        .then(res => {
          console.log(res.data.name);
        })
        .catch(error => {
          console.log(`code: ${error}`);
        });
    });
  })
  .catch(error => {
    console.log(`code: ${error}`);
  });
