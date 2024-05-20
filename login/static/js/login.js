document.getElementById("toggle-cadastro").addEventListener("click", function() {
    var cadastroEmailSenhaForm = document.getElementById("cadastro-email-senha-form");
    var loginForm = document.getElementById("login-form");
    
    if (cadastroEmailSenhaForm.style.display === "none") {
        loginForm.style.display = "none"; 
        cadastroEmailSenhaForm.style.display = "block"; 
    } else {
        loginForm.style.display = "block"; 
        cadastroEmailSenhaForm.style.display = "none"; 
    }
});

document.getElementById("voltar-login").addEventListener("click", function() {
    var cadastroEmailSenhaForm = document.getElementById("cadastro-email-senha-form");
    var loginForm = document.getElementById("login-form");
    
    cadastroEmailSenhaForm.style.display = "none"; 
    loginForm.style.display = "block"; 
});

document.getElementById("proximo-cadastro").addEventListener("click", function(event) {
    // Prevenir o comportamento padrão do botão de submissão
    event.preventDefault();

    // Verificar se o formulário de e-mail e senha é válido
    var cadastroEmailSenhaForm = document.getElementById("cadastro-email-senha-form");
    if (!cadastroEmailSenhaForm.checkValidity()) {
        // Se o formulário não for válido, exibir mensagem de erro e impedir o envio
        cadastroEmailSenhaForm.reportValidity();
        return false;
    }

    // Validar a senha
    var cadastroSenha = document.getElementById("cadastro-senha").value;
    var senhaValida = cadastroSenha.length >= 6 && /[A-Z]/.test(cadastroSenha) && /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(cadastroSenha);

    var validationMessageElement = document.getElementById("senha-validation-message-cadastro");
    if (!senhaValida) {
        // Se a senha não for válida, exibir mensagem de erro
        validationMessageElement.textContent = "A senha deve ter pelo menos 6 caracteres, incluindo um caractere especial e uma letra maiúscula.";
        return false;
    }

    // Limpar qualquer mensagem de erro anterior da senha
    validationMessageElement.textContent = ""; 

    // Se o e-mail e a senha forem válidos, prosseguir para o próximo formulário
    var proximoCadastroForm = document.getElementById("cadastro-form");
    cadastroEmailSenhaForm.style.display = "none";
    proximoCadastroForm.style.display = "block";

    // Evitar que o formulário de login seja ativado
    event.stopPropagation();
    return false;
});











document.getElementById("deficiencia").addEventListener("change", function() {
    var descricaoDeficienciaContainer = document.getElementById("descricao-deficiencia-container");
    var descricaoDeficienciaInput = document.getElementById("descricao-deficiencia");

    if (this.checked) {
        descricaoDeficienciaContainer.style.display = "block";
        descricaoDeficienciaInput.value = ""; 
    } else {
        descricaoDeficienciaContainer.style.display = "none";
        descricaoDeficienciaInput.value = ""; 
    }
});


document.getElementById("next-btn").addEventListener("click", function() {
    var cadastroForm = document.getElementById("cadastro-form");

    if (cadastroForm.checkValidity()) {
        var categoria = document.getElementById("categoria").value;
        cadastroForm.style.display = "none";
        
        if (categoria === "estudante") {
            document.getElementById("estudante-form").style.display = "block";
        } else if (categoria === "pos-graduacao") {
            document.getElementById("pos-graduacao-form").style.display = "block";
        } else if (categoria === "profissional") {
            document.getElementById("profissional-form").style.display = "block";
        }
    } else {
        cadastroForm.reportValidity();
    }
});

document.getElementById("cpf").addEventListener("input", function() {
    var cpfInput = this.value.replace(/\D/g, ''); 
    if (cpfInput.length > 11) {
        cpfInput = cpfInput.slice(0, 11); 
    }
    cpfInput = cpfInput.replace(/(\d{3})(\d)/, '$1.$2'); 
    cpfInput = cpfInput.replace(/(\d{3})(\d)/, '$1.$2'); 
    cpfInput = cpfInput.replace(/(\d{3})(\d{1,2})$/, '$1-$2'); 
    this.value = cpfInput; 
});

document.getElementById("celular").addEventListener("input", function() {
    var celularInput = this.value.replace(/\D/g, ''); 
    if (celularInput.length > 11) {
        celularInput = celularInput.slice(0, 11); 
    }
    celularInput = celularInput.replace(/^(\d{2})(\d)/g, '($1) $2'); 
    celularInput = celularInput.replace(/(\d{5})(\d)/, '$1-$2'); 
    this.value = celularInput; 
});

document.getElementById("login-senha").addEventListener("input", function() {
    // var senha = this.value;
    // var forca = zxcvbn(senha);
    // var feedbackElement = document.getElementById("senha-feedback");
    
    // var senhaValida = senha.length >= 6 && /[A-Z]/.test(senha) && /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(senha);
    
    // if (forca.score >= 3 && senhaValida) {
    //     feedbackElement.innerHTML = "Força da senha: Forte";
    // } else {
    //     feedbackElement.innerHTML = "Força da senha: Fraca";
    // }
});

document.getElementById("cadastro-senha").addEventListener("input", function() {
    var senha = this.value;
    var forca = zxcvbn(senha);
    var feedbackElement = document.getElementById("senha-feedback-cadastro");
    
    var senhaValida = senha.length >= 6 && /[A-Z]/.test(senha) && /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(senha);
    
    if (forca.score >= 3 && senhaValida) {
        feedbackElement.innerHTML = "Força da senha: Forte";
    } else {
        feedbackElement.innerHTML = "Força da senha: Fraca";
    }
});

document.getElementById("login-form").addEventListener("submit", function(event) {
    // var senha = document.getElementById("login-senha").value;
    // var senhaValida = senha.length >= 6 && /[A-Z]/.test(senha) && /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(senha);
    
    // var validationMessageElement = document.getElementById("senha-validation-message");
    // if (!senhaValida) {
    //     validationMessageElement.textContent = "A senha deve ter pelo menos 6 caracteres, incluindo um caractere especial e uma letra maiúscula.";
    //     event.preventDefault(); 
    // } else {
    //     validationMessageElement.textContent = ""; 
    // }
});

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

document.getElementById("descricao-deficiencia").addEventListener('input', function() {
    var valorAnterior = this.value;
    var valorAtual = valorAnterior.replace(/[^A-Za-zÀ-ÖØ-öø-ÿ\s]/g, ''); 
    if (valorAnterior !== valorAtual) {
        this.value = valorAtual;
    }
});

document.getElementById("matricula").addEventListener("input", function() {
    this.value = this.value.replace(/\D/g, '');
});

// Selecionar todos os botões com a classe 'voltar-cadastro-btn'
var voltarCadastroBtns = document.querySelectorAll('.voltar-cadastro-btn');

// Adicionar um evento de clique a cada botão
voltarCadastroBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
        var cadastroForm = document.getElementById("cadastro-form");
        var cadastroEmailSenhaForm = document.getElementById("cadastro-email-senha-form");
        var estudanteForm = document.getElementById("estudante-form");
        var posGraduacaoForm = document.getElementById("pos-graduacao-form");
        var profissionalForm = document.getElementById("profissional-form");

        // Verificar qual formulário está ativo e voltar para o anterior
        if (cadastroEmailSenhaForm.style.display === "block") {
            cadastroEmailSenhaForm.style.display = "none";
            loginForm.style.display = "block";
        } else if (cadastroForm.style.display === "block") {
            cadastroForm.style.display = "none";
            cadastroEmailSenhaForm.style.display = "block";
        } else if (estudanteForm.style.display === "block" || posGraduacaoForm.style.display === "block" || profissionalForm.style.display === "block") {
            cadastroForm.style.display = "block";
            estudanteForm.style.display = "none";
            posGraduacaoForm.style.display = "none";
            profissionalForm.style.display = "none";
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
document.querySelector(".toggle-password").addEventListener("click", togglePasswordVisibility);

function togglePasswordVisibilityLogin() {
    var senhaInput = document.getElementById("login-senha");
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
document.querySelector(".toggle-password").addEventListener("click", togglePasswordVisibilityLogin);
