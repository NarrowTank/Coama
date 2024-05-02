document.addEventListener('DOMContentLoaded', function() {
  const carousel2 = document.querySelector('.carousel2');
  const carouselItemWidth2 = carousel2.firstElementChild.clientWidth; /* Largura de uma imagem no carrossel */
  
  function moveCarousel2() {
    carousel2.style.transition = 'transform 0.5s ease';
    carousel2.style.transform = `translateX(-${carouselItemWidth2}px)`; /* Move o carrossel para a esquerda */
    setTimeout(function() {
      carousel2.appendChild(carousel2.firstElementChild); /* Move a primeira imagem para o final */
      carousel2.style.transition = 'none'; /* Remove a transição para evitar atrasos */
      carousel2.style.transform = 'translateX(0)'; /* Reseta a posição do carrossel */
    }, 500); /* Tempo da transição em milissegundos */
  }
  
  setInterval(moveCarousel2, 3000); /* Move o carrossel automaticamente a cada 3 segundos */
});
