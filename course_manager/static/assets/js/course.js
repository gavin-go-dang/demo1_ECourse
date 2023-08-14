$(function () {

  // Initiate masonry grid
  var $grid = $('.gallery-wrapper').masonry({
    itemSelector: '.grid-item',
    columnWidth: '.grid-sizer',
    percentPosition: true,
  });

  // Initiate imagesLoaded
  $grid.imagesLoaded().progress(function () {
    $grid.masonry('layout');
  });

});



//Select 1 option in filter
$("input:checkbox").on('click', function () {
  var $box = $(this);
  if ($box.is(":checked")) {
    var group = "input:checkbox[name='" + $box.attr("name") + "']";
    $(group).prop("checked", false);
    $box.prop("checked", true);
  } else {
    $box.prop("checked", false);
  }
});

var text = document.querySelector('.description');
var words = text.textContent.split(' ');

if (words.length > 100) {
  text.textContent = words.slice(0, 100).join(' ') + '...';
}