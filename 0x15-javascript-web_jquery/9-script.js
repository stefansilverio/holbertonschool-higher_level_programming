let tag = $('html').attr('lang');
$.get('https://fourtonfish.com/hellosalut/?lang=' + tag, function (resp) {
  let data = resp.hello;
  $('DIV#hello').text(data);
});
