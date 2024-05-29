var inputs = document.querySelectorAll('#nome, #nome-cracha, #cidade, #curso, #instituicao, #area-atuacao, #instituicao-pos'); 
inputs.forEach(function(input) {
    input.addEventListener('input', function(event) {
        var valorAnterior = this.value;
        var valorAtual = valorAnterior.replace(/[^A-Za-zÀ-ÖØ-öø-ÿ\s]/g, ''); 
        if (valorAnterior !== valorAtual) {
            this.value = valorAtual;
        }
    });
});


