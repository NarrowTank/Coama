window.onscroll = function() {myFunction()};

var header = document.getElementById("main-heather");
var first_element = document.getElementById("first_element");
var sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
    first_element.classList.add("content");
  } else {
    header.classList.remove("sticky");
    first_element.classList.remove("content");
  }
}