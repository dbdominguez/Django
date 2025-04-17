console.log("Archivo carrito.js cargado correctamente");

// Array para almacenar los productos del carrito
let carrito = [];

// Seleccionar elementos del DOM
const carritoContainer = document.getElementById("carrito");
const totalElement = document.getElementById("total");
const vaciarCarritoButton = document.getElementById("vaciarCarrito");
const finalizarCompraButton = document.getElementById("finalizarCompra");
const seccionProductos = document.getElementById("seccion-productos");
const seccionEnvio = document.getElementById("seccion-envio");
const seccionPrecio = document.getElementById("seccion-precio");
const volverProductosButton = document.getElementById("volverProductos");
const volverEnvioButton = document.getElementById("volverEnvio");
const resumenProductos = document.getElementById("resumen-productos");
const resumenMetodo = document.getElementById("resumen-metodo");
const totalPrecioElement = document.getElementById("total-precio");
const tipoDocumentoSelect = document.getElementById("tipo-documento");
const documentoGenerado = document.getElementById("documento-generado");

// Función para agregar un producto al carrito
function agregarAlCarritoDesdeHTML(button) {
    console.log("Función agregarAlCarritoDesdeHTML ejecutada");

    const nombre = button.getAttribute("data-nombre");
    const descripcion = button.getAttribute("data-descripcion");
    const precio = parseInt(button.getAttribute("data-precio"));

    const producto = { nombre, descripcion, precio };

    carrito.push(producto);

    console.log("Carrito actualizado:", carrito);

    localStorage.setItem("carrito", JSON.stringify(carrito));

    console.log("Contenido de localStorage después de agregar:", localStorage.getItem("carrito"));

    if (carritoContainer) {
        actualizarCarrito();
    }
}

// Función para actualizar el carrito en el DOM
function actualizarCarrito() {
    console.log("Función actualizarCarrito ejecutada");

    if (!carritoContainer) {
        console.warn("El elemento con ID 'carrito' no existe en esta página.");
        return;
    }

    carritoContainer.innerHTML = "";

    let total = 0;

    carrito.forEach((producto, index) => {
        total += producto.precio;

        const productoHTML = `
            <div class="col-md-12 mb-3">
                <div class="card">
                    <div class="card-body d-flex justify-content-between align-items-center">
                        <div>
                            <h5 class="card-title mb-1"><strong>${producto.nombre}</strong></h5>
                            <p class="card-text mb-1">${producto.descripcion}</p>
                            <p class="card-text mb-1"><strong>Precio:</strong> $${producto.precio}</p>
                        </div>
                        <button class="btn btn-danger" onclick="eliminarDelCarrito(${index})">Eliminar</button>
                    </div>
                </div>
            </div>
        `;
        carritoContainer.innerHTML += productoHTML;
    });

    if (totalElement) {
        totalElement.textContent = total;
    }

    // Actualizar el total en la sección de precio
    if (totalPrecioElement) {
        totalPrecioElement.textContent = total;
    }

    console.log("Carrito mostrado en el DOM:", carrito);
}

// Función para eliminar un producto del carrito
function eliminarDelCarrito(index) {
    console.log(`Eliminando producto en la posición ${index}`);

    carrito.splice(index, 1);

    console.log("Carrito después de eliminar:", carrito);

    localStorage.setItem("carrito", JSON.stringify(carrito));

    console.log("Contenido de localStorage después de eliminar:", localStorage.getItem("carrito"));

    actualizarCarrito();
}

// Función para vaciar el carrito
function vaciarCarrito() {
    console.log("Vaciando el carrito...");

    // Vaciar el array del carrito
    carrito = [];

    // Actualizar localStorage
    localStorage.setItem("carrito", JSON.stringify(carrito));

    // Actualizar el DOM
    actualizarCarrito();

    console.log("Carrito vaciado:", carrito);
}

// Vincular el botón "Vaciar Carrito" a la función vaciarCarrito
if (vaciarCarritoButton) {
    vaciarCarritoButton.addEventListener("click", vaciarCarrito);
}

// Mostrar la sección de Envío al hacer clic en "Siguiente" desde Productos
if (finalizarCompraButton) {
    finalizarCompraButton.addEventListener("click", () => {
        console.log("Mostrando la sección de Envío...");

        // Ocultar la sección de Productos y mostrar la de Envío
        seccionProductos.style.display = "none";
        seccionEnvio.style.display = "block";
    });
}

// Mostrar la sección de Precio al hacer clic en "Siguiente" desde Envío
const siguienteEnvioButton = document.querySelector('#seccion-envio button[type="submit"]');
if (siguienteEnvioButton) {
    siguienteEnvioButton.addEventListener("click", (event) => {
        event.preventDefault(); // Evitar el comportamiento predeterminado del formulario
        console.log("Mostrando la sección de Precio...");

        // Ocultar la sección de Envío y mostrar la de Precio
        seccionEnvio.style.display = "none";
        seccionPrecio.style.display = "block";

        // Mostrar el resumen en la sección de Precio
        mostrarResumen();
    });
}
// Botón para volver a la sección de Productos desde Envío
if (volverProductosButton) {
    volverProductosButton.addEventListener("click", (event) => {
        event.preventDefault(); // Evitar el comportamiento predeterminado del botón
        console.log("Volviendo a la sección de Productos...");

        // Ocultar la sección de Envío y mostrar la de Productos
        seccionEnvio.style.display = "none";
        seccionProductos.style.display = "block";
    });
}

// Volver a la sección de Envío al hacer clic en "Volver" desde Precio
if (volverEnvioButton) {
    volverEnvioButton.addEventListener("click", (event) => {
        event.preventDefault(); // Evitar el comportamiento predeterminado del botón
        console.log("Volviendo a la sección de Envío...");

        // Mostrar la sección de Envío y ocultar la de Precio
        seccionPrecio.style.display = "none";
        seccionEnvio.style.display = "block";
    });
}

// Función para mostrar el resumen en la sección de Precio
function mostrarResumen() {
    // Mostrar los productos seleccionados
    resumenProductos.innerHTML = ""; // Limpiar el contenido previo
    carrito.forEach((producto) => {
        const li = document.createElement("li");
        li.className = "list-group-item";
        li.textContent = `${producto.nombre} - $${producto.precio}`;
        resumenProductos.appendChild(li);
    });

    // Mostrar el método de envío o retiro seleccionado
    const metodoSeleccionado = document.getElementById("metodo").value;
    if (metodoSeleccionado === "envio") {
        resumenMetodo.textContent = "Envío a domicilio";
    } else if (metodoSeleccionado === "retiro") {
        resumenMetodo.textContent = "Retiro en local";
    } else {
        resumenMetodo.textContent = "No seleccionado";
    }

    // Mostrar el total de la compra
    const total = carrito.reduce((sum, producto) => sum + producto.precio, 0);
    totalPrecioElement.textContent = total;
}

// Detectar cambios en el menú desplegable para generar boleta o factura
if (tipoDocumentoSelect) {
    tipoDocumentoSelect.addEventListener("change", () => {
        const tipoSeleccionado = tipoDocumentoSelect.value;

        if (tipoSeleccionado) {
            generarDocumento(tipoSeleccionado);
        }
    });
}

// Función para generar el documento (Boleta o Factura)
function generarDocumento(tipo) {
    const total = totalPrecioElement.textContent; // Obtener el total de la compra
    let contenido = "";

    if (tipo === "boleta") {
        contenido = `
            <h4 class="text-center">*** BOLETA DE COMPRA ***</h4>
            <hr>
            <p><strong>Productos:</strong></p>
            <ul>
                ${carrito.map(producto => `<li>${producto.nombre} - $${producto.precio}</li>`).join("")}
            </ul>
            <p><strong>Total:</strong> $${total}</p>
            <p class="text-center">Gracias por tu compra.</p>
        `;
    } else if (tipo === "factura") {
        contenido = `
            <h4 class="text-center">*** FACTURA ***</h4>
            <hr>
            <p><strong>Productos:</strong></p>
            <ul>
                ${carrito.map(producto => `<li>${producto.nombre} - $${producto.precio}</li>`).join("")}
            </ul>
            <p><strong>Total:</strong> $${total}</p>
            <p><strong>Razón Social:</strong> [Nombre de la Empresa]</p>
            <p><strong>RUT:</strong> [12345678-9]</p>
            <p class="text-center">Gracias por tu compra.</p>
        `;
    }

    // Mostrar el contenido generado en el contenedor
    documentoGenerado.innerHTML = contenido;
    documentoGenerado.style.display = "block"; // Hacer visible el contenedor
}

// Cargar el carrito desde localStorage al iniciar (solo si estamos en la página del carrito)
if (carritoContainer) {
    document.addEventListener("DOMContentLoaded", () => {
        console.log("Evento DOMContentLoaded ejecutado");

        const carritoGuardado = localStorage.getItem("carrito");
        console.log("Cargando carrito desde localStorage:", carritoGuardado);

        if (carritoGuardado) {
            carrito = JSON.parse(carritoGuardado);
            actualizarCarrito();
        }
    });
}
