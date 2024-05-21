function toggleContent(target) {
    const contentDivs = document.querySelectorAll(".second-column > div");
    contentDivs.forEach(div => {
        div.style.display = "none";
    });
    document.querySelector("." + target).style.display = "flex";
    // Se a tela for menor que 1040px, também aplicamos o mesmo estado de exibição ao segundo contêiner
    if (window.innerWidth < 1040) {
        document.querySelector(".container-main-mobile ." + target).style.display = "flex";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    // Mostrar os dados pessoais logo quando a página for carregada
    document.querySelector(".dados-pessoais").style.display = "flex";

    const navItems = document.querySelectorAll(".nav-item");
    navItems.forEach(item => {
        item.addEventListener("click", function() {
            const target = item.getAttribute("data-target");
            toggleContent(target);
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    // Mostrar os dados pessoais logo quando a página for carregada
    document.querySelector(".container-main-mobile .dados-pessoais").style.display = "flex";

    const navItems = document.querySelectorAll(".menu-principal-container-mobile .nav-item");
    navItems.forEach(item => {
        item.addEventListener("click", function() {
            const target = item.getAttribute("data-target");
            toggleContent(target);
        });
    });
});

// Adicionando manipulador de evento de redimensionamento para sincronizar alterações quando a janela é redimensionada
window.addEventListener("resize", function() {
    const currentDisplay = document.querySelector(".second-column > div[style='display: flex;']");
    if (currentDisplay) {
        const target = currentDisplay.classList[0];
        toggleContent(target);
    }
});



function abrirDialog() {
    document.querySelector('.dialog-container').style.display = 'flex';
}

function fecharDialog() {
    document.querySelector('.dialog-container').style.display = 'none';
}

var fileUpload = document.getElementById("fileUpload");
var btnEnviar = document.getElementById("submitBtn");
btnEnviar.addEventListener("click", function () {
    document.getElementById("fileUpload").classList.remove("invalid");

    if (fileUpload.files.length === 0){
        fileUpload.classList.add("invalid");
    }

    if (fileUpload.files.length === 0) {
        abrirDialog();
    }
});

var fileUploadMobile = document.getElementById("fileUploadMobile");
var btnEnviarMobile = document.getElementById("submitBtnMobile");
btnEnviarMobile.addEventListener("click", function () {
    document.getElementById("fileUploadMobile").classList.remove("invalid");

    if (fileUploadMobile.files.length === 0){
        fileUploadMobile.classList.add("invalid");
    }

    if (fileUploadMobile.files.length === 0) {
        abrirDialog();
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const boxes = document.querySelectorAll('.box');

    boxes.forEach(box => {
        const editButton = box.querySelector('.button-editar');
        const cancelButton = box.querySelector('.button-cancelar');
        const confirmButton = box.querySelector('.button-confirmar');
        const input = box.querySelector('input, select');
        const p = box.querySelector('p');

        if (editButton && cancelButton && confirmButton && input && p) {
            editButton.addEventListener('click', () => {
                editButton.disabled = true;
                input.style.display = 'inline-block';
                cancelButton.style.display = 'inline-block';
                confirmButton.style.display = 'inline-block';
                p.style.display = 'none';
            });

            cancelButton.addEventListener('click', () => {
                editButton.disabled = false;
                input.style.display = 'none';
                cancelButton.style.display = 'none';
                confirmButton.style.display = 'none';
                p.style.display = 'block';
            });

            confirmButton.addEventListener('click', () => {
                // Valida se o campo de input é válido
                if (!input.checkValidity()) {
                    // Se não for válido, mostra a mensagem padrão de validação do HTML
                    input.reportValidity();
                    return; // Impede que a função prossiga se o input não estiver válido
                }

                editButton.disabled = false;
                input.style.display = 'none';
                cancelButton.style.display = 'none';
                confirmButton.style.display = 'none';
                p.style.display = 'block';

                // Atualiza o conteúdo da tag <p> com o valor do input
                if (input.tagName === 'SELECT') {
                    p.textContent = input.options[input.selectedIndex].text;
                } else {
                    p.textContent = input.value;
                }
            });
        }
    });
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

document.getElementById("celular-mobile").addEventListener("input", function() {
    var celularInput = this.value.replace(/\D/g, ''); 
    if (celularInput.length > 11) {
        celularInput = celularInput.slice(0, 11); 
    }
    celularInput = celularInput.replace(/^(\d{2})(\d)/g, '($1) $2'); 
    celularInput = celularInput.replace(/(\d{5})(\d)/, '$1-$2'); 
    this.value = celularInput; 
});

document.getElementById("matricula").addEventListener("input", function() {
    this.value = this.value.replace(/\D/g, '');
});

document.getElementById("matricula-mobile").addEventListener("input", function() {
    this.value = this.value.replace(/\D/g, '');
});

var inputs = document.querySelectorAll('#nome, #nome-cracha, #cidade, #curso, #instituicao'); 
inputs.forEach(function(input) {
    input.addEventListener('input', function(event) {
        var valorAnterior = this.value;
        var valorAtual = valorAnterior.replace(/[^A-Za-zÀ-ÖØ-öø-ÿ\s]/g, ''); 
        if (valorAnterior !== valorAtual) {
            this.value = valorAtual;
        }
    });
});

var inputs = document.querySelectorAll('#nome-mobile, #nome-cracha-mobile, #cidade-mobile, #curso-mobile, #instituicao-mobile'); 
inputs.forEach(function(input) {
    input.addEventListener('input', function(event) {
        var valorAnterior = this.value;
        var valorAtual = valorAnterior.replace(/[^A-Za-zÀ-ÖØ-öø-ÿ\s]/g, ''); 
        if (valorAnterior !== valorAtual) {
            this.value = valorAtual;
        }
    });
});




