$.get('https://swapi.co/api/people/5/?format=json', function (resp) {
  $('DIV#character').text(resp.name);
});
