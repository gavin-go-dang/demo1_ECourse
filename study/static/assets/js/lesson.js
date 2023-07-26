//sidebar
function hasClass(ele, cls) {
  return !!ele.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
}

function addClass(ele, cls) {
  if (!hasClass(ele, cls)) ele.className += " " + cls;
}

function removeClass(ele, cls) {
  if (hasClass(ele, cls)) {
    const reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
    ele.className = ele.className.replace(reg, ' ');
  }
}

function init() {
  $("#open-menu").click(toggleMenu);
  $("#body-overlay").click(toggleMenu);
}

//The actual fuction
function toggleMenu() {
  const ele = document.getElementsByTagName('body')[0];
  if (!hasClass(ele, "menu-open")) {
    addClass(ele, "menu-open");
  } else {
    removeClass(ele, "menu-open");
  }
}

//Prevent the function to run before the document is loaded
document.addEventListener('readystatechange', function () {
  if (document.readyState === "complete") {
    init();
  }
});

//lesson learned
// $(document).ready(function() {
//   const video = $('video#lesson-video')[0];
//   let printed = false;
//   $(video).on('timeupdate', function() {
//     const watchedPercent = (this.currentTime / this.duration) * 100;
//     if (watchedPercent >= 90 && !printed) {
//       console.log(this.currentTime);
//       printed = true;
//     }
//   });
// });