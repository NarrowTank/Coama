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

// Função para alternar a visibilidade da senha
function togglePasswordVisibility() {
    var senhaInput = document.getElementById("cadastro-senha");
    var senhaIcon = document.querySelector(".toggle-password");

    if (senhaInput.type === "password") {
        senhaInput.type = "text";
        senhaIcon.classList.remove("fa-eye-slash");
        senhaIcon.classList.add("fa-eye");
    } else {
        senhaInput.type = "password";
        senhaIcon.classList.remove("fa-eye");
        senhaIcon.classList.add("fa-eye-slash");
    }
}

// Adicionar evento de clique ao ícone para alternar a visibilidade da senha
// document.querySelector(".toggle-password").addEventListener("click", togglePasswordVisibility);

// function togglePasswordVisibilityLogin() {
//     var senhaInput = document.getElementById("login-senha");
//     var senhaIcon = document.querySelector(".toggle-password");

//     if (senhaInput.type === "password") {
//         senhaInput.type = "text";
//         senhaIcon.classList.remove("fa-eye-slash");
//         senhaIcon.classList.add("fa-eye");
//     } else {
//         senhaInput.type = "password";
//         senhaIcon.classList.remove("fa-eye");
//         senhaIcon.classList.add("fa-eye-slash");
//     }
// }

// // Adicionar evento de clique ao ícone para alternar a visibilidade da senha
// document.querySelector(".toggle-password").addEventListener("click", togglePasswordVisibilityLogin);
