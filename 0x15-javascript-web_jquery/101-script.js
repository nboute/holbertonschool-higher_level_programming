$(document).ready(function () {
  $('#add_item').click(function () {
    console.log('A');
    $('ul.my_list').prepend('<li>Item</li>');
  });

  $('#remove_item').click(function () {
    console.log('B');
    $('ul.my_list li').last().remove();
  });

  $('#clear_list').click(function () {
    console.log('C');
    $('ul.my_list').empty();
  });
});
