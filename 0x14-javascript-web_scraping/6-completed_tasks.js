#!/usr/bin/node

const axios = require('axios');

const users = {};

for (let i = 1; i < 11; i++) {
  users[i] = 0;
}

axios
  .get('https://jsonplaceholder.typicode.com/todos')
  .then(res => {
    res.data.forEach(function (task) {
      if (task.completed === true) {
        users[task.userId] += 1;
      }
    });
    console.log(users);
  })
  .catch(error => {
    console.log(`code: ${error}`);
  });
