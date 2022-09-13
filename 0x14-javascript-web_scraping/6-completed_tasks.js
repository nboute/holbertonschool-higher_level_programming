#!/usr/bin/node

const axios = require('axios');

const users = {};

axios
  .get('https://jsonplaceholder.typicode.com/todos')
  .then(res => {
    res.data.forEach(function (task) {
      if (task.completed === true) {
        if (users[task.userId] == undefined) {
          users[task.userId] = 0;
        }
        users[task.userId] += 1;
      }
    });
    console.log(users);
  })
  .catch(error => {
    console.log(`code: ${error}`);
  });
