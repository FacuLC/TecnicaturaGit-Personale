// creamos las contantes de las pantallas del carrito
const modalContainer = document.getElementById('modal-container');
const modalOverlay = document.getElementById('modal-overlay');

// aca traemos el id del boton del carrito
const cartBtn = document.getElementById('cart-btn');

// agregamos el contador de productos
const cartCounter = document.getElementById('cart-counter');

//Creamos la contante que muestra la pantalla del carrito
const displayCart = () => {
    //para que no se duplique el contenido del boton del carrito
    modalContainer.innerHTML = "";

    //Aca nosotros hacemos que la pantalla del carrito se muestre
    modalContainer.style.display = "block";
    modalOverlay.style.display = "block";
   
    //Creamos la cabeza de la pantalla del carrito
    const modalHeader = document.createElement("div");
    
    //creamos el botón que cierra la pantalla del carrito
    const modalClose = document.createElement("div");
    modalClose.innerText = "❌"
    modalClose.className = "modal-close"; // asiganamos el nombre para cerrar la pantalla del carrito

    //caundo hacemos click en la ❌ se cierra la pantalla del carrito
    modalClose.addEventListener("click", () =>{
        modalContainer.style.display = "none";
        modalOverlay.style.display = "none";
    })

    // aca agregamos la ❌ a la pantalla del carrito
    modalHeader.append(modalClose);

    //creamos el texto de la pantalla del carrito
    const modalTitle = document.createElement("div")
    modalTitle.innerText = "Carrito" // aca agregamos el texto de la pantalla del carrito
    modalTitle.className = "modal-title"

    modalHeader.append(modalTitle)

    //agregamos todo lo anterior al contenedor del carrito
    modalContainer.append(modalHeader);

    // aca agregamos el texto si el carrito no tiene ningun producto dentro (con un if-else)
    if(cart.length > 0){

    // mostramos los productos que estan en el carrito(body del header)
    cart.forEach((product) => {
        const modalBody = document.createElement("div");
        modalBody.className = "modal-body";
        modalBody.innerHTML = `
        <div class = "product">

          <img class = "product.img" src = "${product.img}" />
          <div class = "product-info">
            <h4>${product.productName}<h4>
          </div>
          
          <div class = "quantity">
          <span class = "quantity-btn-decrese">➖</span>
          <span class = "quantity-input">${product.quanty}</span>
          <span class = "quantity-btn-increse">➕</span>
          </div>
          
          <div class = "price">${product.price * product.quanty} $</div>
          <div class = "delete-product">❌</div>

        </div>
        `;
        modalContainer.append(modalBody);
        
        //Funcion de boton resta (querySelector) captura la clase del boton de -
        const decrese = modalBody.querySelector(".quantity-btn-decrese");
        decrese.addEventListener("click", () => {
            if(product.quanty !==1)
            product.quanty--;
            displayCart()

            displayCartCounter();
        });

        //Boton de suma
        
        const increse = modalBody.querySelector(".quantity-btn-increse")
        increse.addEventListener("click", () => {
            product.quanty++;
            displayCart();

            displayCartCounter();
        })

        // Creamos el boton para eliminar productos del carrito

        const deleteProduct = modalBody.querySelector(".delete-product");

        //
        deleteProduct.addEventListener("click", () => {
            deleteCartProduct(product.id);
        });

    });

        const total = cart.reduce((acumulate, element) => acumulate + element.price * element.quanty, 0);

        // creamos el pie del carrito
        const modalFooter = document.createElement('div');
        modalFooter.className = "modal-footer";
        modalFooter.innerHTML = `
        <div class = "total-price">Precio Total a Pagar: ${total} $</div>
        <button class = "btn-primary" id = "checkout-btn"> Realizar el Pago </button>
        <div id = "button-checkout"></div>
        `;
        modalContainer.append(modalFooter);
        //MP
        const mercadopago = new MercadoPago("TEST-8b9b4df7-1b07-4fe7-a832-216563d59d53",{
        locale: "es-AR", //tipos de monedas'pt-BR'
    });

    const checkoutButton = modalFooter.querySelector("#checkout-btn");

    checkoutButton.addEventListener("click", function () {

        checkoutButton.remove();

        const orderData = {
            quantity: 1,
            description: "Gracias por tu Compra",
            price: total,
        };

        fetch("http://localhost:8080/create_preference",{
            method: "POST",
            headers: {
                "Content-Type":"application/json",
            },
            body: JSON.stringify(orderData),
        })
            .then(function (response) {
                return response.json();
            })
            .then(function (preference) {
                createCheckoutButton(preference.id);
            })
            .catch(function() {
                alert("Unexpected error");
            });
    });

        function createCheckoutButton(preferenceId){
            //Inicializamos el Checkout

            const bricksBuilder = mercadopago.bricks();

            const renderComponent = async (bricksBuilder) => {
            

                await bricksBuilder.create(
                    "wallet",
                    "button-checkout",
                    {
                        initialization: {
                            preferenceId: preferenceId,
                        },
                        callbacks: {
                            onError: (error) => console.error(error),
                            onReady: () => {},
                        },
                    }
                )
            };

            window.checkoutButton = renderComponent(bricksBuilder);
        }
}else{
    const modalText = document.createElement("h2");
    modalText.className = "modal-body1";
    modalText.innerText = "Tu carrito esta Vacio";
    modalContainer.append(modalText);
}
};

// ahora cuando hagamos click en el carrito se mostrara la pantalla del carrito

cartBtn.addEventListener("click", displayCart);

//usamos la funcion (findIndex) sirve para saber en q posiscion esta ubicado el producto del carrito
const deleteCartProduct = (id) =>{
    const foundId = cart.findIndex((element)=> element.id === id)
    console.log(foundId)
    // splice elimina producto del carrito o array (tenes que decirle cuantos productos)
    cart.splice(foundId, 1);
    //aca volvemos a mostrar el carrito para que se muestre el cambio
    displayCart();

    displayCartCounter();
};

// creamos la funcion donde muestra la cantidad de productos del carrito
const displayCartCounter = () => {
    const cartQuanty = cart.reduce((acumulate, element) => acumulate + element.quanty, 0);
    cartCounter.style.display = "block";
    cartCounter.innerText = cartQuanty;
}