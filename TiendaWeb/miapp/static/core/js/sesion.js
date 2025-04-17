document.addEventListener("DOMContentLoaded", function() {
    let email = localStorage.getItem("email");
    let role = localStorage.getItem("role");

    if (email) {
        console.log("Usuario autenticado:", email, "Rol:", role);
    } else {
        console.log("No hay usuario autenticado.");
    }

    // Modificar botón "Iniciar Sesión" para redirigir si ya hay sesión iniciada
    let btnIniciarSesion = document.getElementById("btnIniciarSesion");
    let modalInicioSesion = new bootstrap.Modal(document.getElementById("ModalInicioSecion"));

    if (btnIniciarSesion) {
        btnIniciarSesion.addEventListener("click", function(event) {
            if (email) {
                // Redirigir según el rol
                if (role === "admin") {
                    window.location.href = "../TrabajoWeb/HTML/Paginas_Principales/Perfil-Admin.html";
                } else {
                    window.location.href = "../TrabajoWeb/HTML/Paginas_Principales/Perfil.html";
                }
            } else {
                // Abrir el modal si no hay sesión iniciada
                modalInicioSesion.show();
            }
        });
    }
});

// Manejar el inicio de sesión en el modal
document.getElementById("FormularioInicio").addEventListener("submit", function(event) {
    event.preventDefault();

    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value.trim();

    // Obtener usuarios
    let usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];

    // Buscar usuario
    let usuarioEncontrado = usuarios.find(user => user.email === email && user.password === password);

    if (usuarioEncontrado) {
        // Guardar sesión
        localStorage.setItem("email", usuarioEncontrado.email);
        localStorage.setItem("role", usuarioEncontrado.role);

        console.log("Inicio de sesión exitoso:", usuarioEncontrado);

        // Cerrar modal
        let modalElement = document.getElementById('ModalInicioSecion');
        let modal = bootstrap.Modal.getInstance(modalElement);
        if (modal) modal.hide();

        // Redirigir según el rol
        setTimeout(() => {
            if (usuarioEncontrado.role === "admin") {
                window.location.href = "../TrabajoWeb/HTML/Paginas_Principales/Perfil-Admin.html"; 
            } else {
                window.location.href = "../TrabajoWeb/HTML/Paginas_Principales/Perfil.html";
            }
        }, 500);
    } else {
        alert("Credenciales incorrectas. Intenta de nuevo.");
    }
});

// Cierre de sesión
document.getElementById("logout")?.addEventListener("click", function() {
    localStorage.clear();

    let redirectPath = window.location.pathname.includes("Paginas_Principales") ? "../../Index.html" : "Index.html";

    window.location.href = redirectPath;
});

// Redireccionar Icono de perfil
document.addEventListener("DOMContentLoaded", function() {
    let perfilIcono = document.getElementById("iconoPerfil");
    let modalInicioSesion = new bootstrap.Modal(document.getElementById("ModalInicioSecion"));

    if (perfilIcono) {
        perfilIcono.addEventListener("click", function(event) {
            let email = localStorage.getItem("email");
            let role = localStorage.getItem("role");

            if (email) {
                if (role === "admin") {
                    window.location.href = "../TrabajoWeb/HTML/Paginas_Principales/Perfil-Admin.html";
                } else {
                    window.location.href = "../TrabajoWeb/HTML/Paginas_Principales/Perfil.html"; 
                }
            } else {
                event.preventDefault();
                modalInicioSesion.show();
            }
        });
    }
});

// Forzar cerrado modal
document.addEventListener("hidden.bs.modal", function () {
    let backdrop = document.querySelector(".modal-backdrop");
    if (backdrop) backdrop.remove();
    document.body.classList.remove("modal-open");
});