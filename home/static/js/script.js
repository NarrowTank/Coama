let count = 1;
document.getElementById("radio1").checked = true;

setInterval( function(){
nextImage();
}, 5000)

function nextImage(){
    count++;
    if(count>3){
        count = 1;
    }

    document.getElementById("radio" + count).checked = true;
}

window.onscroll = function() {myFunction()};

var header = document.getElementById("main-heather");
var sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}