const contenedorCarrito = document.getElementById("contenedor-carrito");
const sobrePantalla = document.getElementById("sobre-pantalla");

const carritoCompras = document.getElementById("carrito-compras");

const mostrarCarrito =() => {
    contenedorCarrito.innerHTML = "";
    contenedorCarrito.style.display = "block";
    sobrePantalla.style.display = "block";

    //Modelo de Cabezera
    const modeloCabezara = document.createElement("div");

    const modeloCerrar = document.createElement("div");
    modeloCerrar.innerText = "❌"
    modeloCerrar.className = "modelo-cerrar";
    modeloCabezara.append(modeloCerrar);

    modeloCabezara.addEventListener("click", () => {
        contenedorCarrito.style.display = "none";
        sobrePantalla.style.display = "none";
    })

    const modeloTitulo = document.createElement("div");
    modeloTitulo.innerText = "Carrito";
    modeloTitulo.className = "modelo-titulo";
    modeloCabezara.append(modeloTitulo);

    contenedorCarrito.append(modeloCabezara);

    // Modelo del Cuerpo
    carrito.forEach((product) => {
        const modeloCuerpo = document.createElement("div");
        modeloCuerpo.className = "modelo-cuerpo";
        modeloCuerpo.innerHTML = `
        
        <div class = "producto">
        <img class = "producto-img" src = "${product.img}"></img>
        <div class = "producto-info">
            <h4>${product.nombreProducto}</h4>
        </div>
        
        <div class = "cantidad">
            <span class = "cantidad-btn-menos">-</span>
            <span class = "cantidad-input">${product.cantidad}</span>
            <span class = "cantidad-btn-mas">+</span>
        </div>

        <div class = "precio">${product.precio * product.cantidad} $</div>
        <div class = "eliminar-producto">❌</div>
        </div>
        `;

        contenedorCarrito.append(modeloCuerpo)

        // Boton de menos 
        const menos = modeloCuerpo.querySelector(".cantidad-btn-menos");
        menos.addEventListener("click", () => {
            if(product.cantidad !==1)
            product.cantidad--;
            mostrarCarrito()
        });

        //Boton Mas
        const mas = modeloCuerpo.querySelector(".cantidad-btn-mas");
        mas.addEventListener("click", () => {
            product.cantidad++;
            mostrarCarrito()
        });


        //Eliminar
        const eliminarProducto = modeloCuerpo.querySelector(".eliminar-producto");

        eliminarProducto.addEventListener("click", () => {
            eliminarProducto(product.id);
        })
    })

    //Modelo Pie Pagina

    const total = carritoCompras.reduce((acumulador, elemento) => acumulador + elemento.precio * cantidad, 0)
 
    const modeloPies = document.createElement("div");
    modeloPies.className = "modelo-pies";
    modeloPies.innerHTML = `
    <div class = "total-precio">Total</div>;
    `;
    contenedorCarrito.append(modeloPies);
};

carritoCompras.addEventListener("click", mostrarCarrito)

const eliminarProducto = (id) => {
    const encuentraId = carrito.findIndex((elemento)=> elemento.id === id)
}