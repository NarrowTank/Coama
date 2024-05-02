document.addEventListener("DOMContentLoaded", function() {
    var btnInicio = document.getElementById('btnInicio');
    btnInicio.addEventListener("click", function(event) {
      event.preventDefault(); // Impede o comportamento padrão do botão (navegação)
      scrollToTop(1000); // Função para rolar suavemente para o topo
    });
  });
  
  // Função para rolar suavemente para o topo da página
  function scrollToTop(scrollDuration) {
    var cosParameter = window.scrollY / 2,
        scrollCount = 0,
        oldTimestamp = performance.now();
    function step (newTimestamp) {
      scrollCount += Math.PI / (scrollDuration / (newTimestamp - oldTimestamp));
      if (scrollCount >= Math.PI) window.scrollTo(0, 0);
      if (window.scrollY === 0) return;
      window.scrollTo(0, Math.round(cosParameter + cosParameter * Math.cos(scrollCount)));
      oldTimestamp = newTimestamp;
      window.requestAnimationFrame(step);
    }
    window.requestAnimationFrame(step);
  }