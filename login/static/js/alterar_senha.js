// Função para alternar a visibilidade da senha
function togglePasswordVisibility() {
    var senhaInput = document.getElementById("nova-senha");
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
document.querySelector(".toggle-password").addEventListener("click", togglePasswordVisibility);

function togglePasswordVisibilityLogin() {
    var senhaInput = document.getElementById("repita-senha");
    var senhaIcon = document.querySelector(".toggle-password-dois");

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
document.querySelector(".toggle-password-dois").addEventListener("click", togglePasswordVisibilityLogin);

document.getElementById("nova-senha").addEventListener("input", function() {
    var senha = this.value;
    var forca = zxcvbn(senha);
    var feedbackElement = document.getElementById("senha-feedback");
    var validationMessageElement = document.getElementById("senha-validation-message");
    
    var senhaValida = senha.length >= 6 && /[A-Z]/.test(senha) && /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(senha);
    
    if (forca.score >= 3 && senhaValida) {
        feedbackElement.innerHTML = "Força da senha: Forte";
        validationMessageElement.textContent = "";
    } else {
        feedbackElement.innerHTML = "Força da senha: Fraca";
        validationMessageElement.textContent = "A senha deve ter pelo menos 6 caracteres, incluindo um caractere especial e uma letra maiúscula.";
    }
});

document.getElementById("alterar-senha-form").addEventListener("submit", function(event) {
    var senha = document.getElementById("nova-senha").value;
    var repitaSenha = document.getElementById("repita-senha").value;
    var senhaValida = senha.length >= 6 && /[A-Z]/.test(senha) && /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(senha);
    
    var validationMessageElement = document.getElementById("senha-validation-message");
    var mismatchMessageElement = document.getElementById("senha-mismatch-message");
    
    if (!senhaValida) {
        validationMessageElement.textContent = "A senha deve ter pelo menos 6 caracteres, incluindo um caractere especial e uma letra maiúscula.";
        event.preventDefault(); 
    } else {
        validationMessageElement.textContent = ""; 
    }

    if (senha !== repitaSenha) {
        mismatchMessageElement.textContent = "As senhas não são iguais.";
        event.preventDefault();
    } else {
        mismatchMessageElement.textContent = "";
    }
});