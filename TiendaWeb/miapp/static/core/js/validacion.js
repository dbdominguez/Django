// Confirmar que se está cargando el JS en el navegador
console.log("Archivo validacion.js cargado correctamente");


// Validación de formulario Registro
(function () {
    'use strict';
    
    var forms = document.querySelectorAll('.needs-validation');

    Array.prototype.slice.call(forms).forEach(function (form) {
        form.addEventListener('submit', function (event) {
            var passwordInput = form.querySelector("#password");
            var passwordError = form.querySelector("#passwordError");

            // Expresión para validar la contraseña
            var passwordPattern = /^(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-zA-Z]).{8,16}$/;

            console.log("Contraseña ingresada:", passwordInput.value); // Depuración

            // Validar el formulario
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                console.log("Formulario no válido");
            } else if (!passwordPattern.test(passwordInput.value)) {
                // Si la contraseña no cumple con el patrón
                event.preventDefault();
                event.stopPropagation();
                passwordError.textContent = "La contraseña debe tener entre 8 y 16 caracteres, incluir al menos un número, una letra y un carácter especial.";
                passwordInput.classList.add("is-invalid");
                console.log("Contraseña no válida:", passwordInput.value);
            } else {
                // Si la contraseña es válida
                event.preventDefault();
                passwordInput.classList.remove("is-invalid");
                passwordError.textContent = "";

                console.log("Contraseña válida:", passwordInput.value);

                // Guardar los datos del formulario en localStorage
                guardarDatosEnLocalStorage(form);

                console.log("Redirigiendo a Perfil.html..."); 

                setTimeout(function () {
                    window.location.href = "Perfil.html";
                }, 500);
            }

            form.classList.add('was-validated');
        }, false);
    });
})();

// Función para guardar los datos del formulario en localStorage
function guardarDatosEnLocalStorage(form) {
    // Obtener los valores de los campos del formulario
    const nombres = form.querySelector("#validationCustom01").value;
    const apellidos = form.querySelector("#validationCustom02").value;
    const email = form.querySelector("#validationCustomUsername").value;
    const telefono = form.querySelector("#validationCustom05").value;
    const direccion = form.querySelector("#validationCustom03").value;
    const region = form.querySelector("#validationCustom04").value;
    const password = form.querySelector("#password").value;


    // Crear un objeto con los datos del usuario
    const usuario = {
        nombres,
        apellidos,
        email,
        telefono,
        direccion,
        region,
        password,
    };

    // Guardar el objeto en localStorage
    localStorage.setItem("usuario", JSON.stringify(usuario));

    console.log("Datos del usuario guardados en localStorage:", usuario);
}

// Función para manejar el inicio de sesión
function iniciarSesion(event) {
    event.preventDefault(); // Evitar que el formulario recargue la página

    // Obtener los valores ingresados en el formulario de inicio de sesión
    const emailIngresado = document.getElementById("email").value;
    const passwordIngresado = document.getElementById("password").value;

    // Recuperar los datos del usuario desde localStorage
    const usuarioGuardado = localStorage.getItem("usuario");

    if (usuarioGuardado) {
        const usuario = JSON.parse(usuarioGuardado);

        // Validar el correo y la contraseña
        if (usuario.email === emailIngresado && usuario.password === passwordIngresado) {
            alert("Inicio de sesión exitoso. ¡Bienvenido, " + usuario.nombres + "!");
            console.log("Inicio de sesión exitoso:", usuario);

            // Redirigir a la página principal o perfil
            window.location.href = "Perfil.html";
        } else {
            alert("Correo o contraseña incorrectos. Por favor, inténtalo de nuevo.");
            console.log("Error: Correo o contraseña incorrectos.");
        }
    } else {
        alert("No hay usuarios registrados. Por favor, regístrate primero.");
        console.log("Error: No hay datos en localStorage.");
    }
}