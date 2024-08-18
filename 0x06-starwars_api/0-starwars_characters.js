#!/usr/bin/node

const req = require('request');
const util = require('util');
const promise = util.promisify(req);

const getCharacter = async (url) => {
  const res = await promise(url);
  if (res.statusCode === 200) console.log(JSON.parse(res.body).name);
};
const getCharMovies = async (id) => {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  const res = await promise(url);
  if (res.statusCode === 200) {
    const characters = JSON.parse(res.body).characters;
    for (const character of characters) {
      await getCharacter(character);
    }
  }
};

const movieId = process.argv[2];
getCharMovies(movieId);
