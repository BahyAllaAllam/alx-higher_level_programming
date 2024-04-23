#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
  } else {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    charactersUrls.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else if (charResponse.statusCode !== 200) {
          console.error(`Failed to fetch character details. Status code: ${charResponse.statusCode}`);
        } else {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  }
});
