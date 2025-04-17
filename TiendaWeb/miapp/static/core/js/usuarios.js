document.addEventListener("DOMContentLoaded", function() {
    // Verifica si hay usuarios
    if (!localStorage.getItem("usuarios")) {
        let usuarios = [
            { email: "admin@tienda.com", password: "Admin123!", role: "admin" },
            { email: "cliente@tienda.com", password: "Cliente1!", role: "cliente" }
        ];

        localStorage.setItem("usuarios", JSON.stringify(usuarios));
    }
});