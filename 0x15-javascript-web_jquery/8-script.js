$.get('https://swapi-api.hbtn.io/api/films/?format=json',
  function (data) {
    console.log(data);
    data.results.forEach(function (movie) {
      console.log('hello');
      $('#list_movies').prepend('<li>' + movie.title + '</li>');
    });
  });
