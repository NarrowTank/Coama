document.addEventListener("DOMContentLoaded", function() {
  let carousel = document.querySelector(".carousel-inner");
  let images = document.querySelectorAll(".carousel-inner img");
  let navigation = document.querySelector(".carousel-navigation");
  let currentIndex = 0;
  let totalImages = images.length;


  for (let i = 0; i < totalImages; i++) {
    let navItem = document.createElement("span");
    navItem.classList.add("nav-item");
    if (i === currentIndex) {
      navItem.classList.add("active");
    }
    navItem.addEventListener("click", function() {
      currentIndex = i;
      updateCarousel();
    });
    navigation.appendChild(navItem);
  }

  function updateCarousel() {
    carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
    let navItems = document.querySelectorAll(".nav-item");
    navItems.forEach((item, index) => {
      if (index === currentIndex) {
        item.classList.add("active");
      } else {
        item.classList.remove("active");
      }
    });
  }

  setInterval(() => {
    currentIndex = (currentIndex + 1) % totalImages;
    updateCarousel();
  }, 5000);
});