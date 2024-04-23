#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;
let moviesCount = 0;

request(apiUrl, (_error, response, body) => {
  body = JSON.parse(body).results;
  body.forEach((film) => {
    const characters = film.characters.map((characterUrl) => parseInt(characterUrl.split('/').slice(-2, -1)[0]));
    if (characters.includes(characterId)) {
      moviesCount++;
    }
  });
  console.log(moviesCount);
});
