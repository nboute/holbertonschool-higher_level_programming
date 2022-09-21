$(document).ready(function () {
  $('#btn_translate').click(function () {
    $.post('https://stefanbohacek.com/hellosalut/?lang=' + $('#language_code').val(), function (data) {
      $('#hello').text(data.hello);
    });
  });
});
