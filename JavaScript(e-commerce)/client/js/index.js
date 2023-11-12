// Creamos una Constante para el contenido de la tienda

// el (getElmentById) obtenemos los elmentos por id
const shopContent = document.getElementById('shopContent');

// creamos un arreglo donde va a estar nuestro carrito
const cart = [];

//Llamamos a la funcion constnate donde tenemos los productos
productos.forEach((product) => {
    const content = document.createElement('div');
    content.innerHTML = `
    <img src="${product.img}"/>
    <h3>${product.productName}</h3>
    <p>${product.price} $</p>
    `;
    // agregamos la constante (content) al contenido de la tienda
    shopContent.append(content)

    // agregamos el boton de compra
    
    const buyButton = document.createElement('button');
    buyButton.innerText = "Comprar";

    content.append(buyButton);

    // aca cada vez que nosotros hagamos click se agrega (push) el producto al carrito(cart: que esta vacio)
    buyButton.addEventListener("click", ()=>{
        
        //creamos una constante para saber si el producto ya esta en el carrito
        const repeat = cart.some((repeatProduct) => repeatProduct.id === product.id);// preguntamos si hay un (id) repetido
                    //some, busca una coincidencia de los (id,s de los productos)
        if(repeat) {
            cart.map((prod) => {//map busca y detecta si hay id,s igual a los q el usuario esta selecionando
                if(prod.id === product.id){
                    prod.quanty ++;
                    displayCartCounter();
                };
            });
        }else{
            cart.push({
                id : product.id,
                productName : product.productName,
                price : product.price,
                quanty : product.quanty,
                img : product.img,
            });
            displayCartCounter();
        };
        console.log(cart)
    });

});