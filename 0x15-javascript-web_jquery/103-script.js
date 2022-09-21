$(document).ready(function () {
  $('#btn_translate').click(function () {
    $.post('https://stefanbohacek.com/hellosalut/?lang=' + $('#language_code').val(), function (data) {
      $('#hello').text(data.hello);
    });
  });
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      event.preventDefault();
      $('#btn_translate').click();
    }
  });
});
