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

