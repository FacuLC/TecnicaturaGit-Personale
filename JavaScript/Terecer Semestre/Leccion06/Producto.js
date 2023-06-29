class Producto{
    static contadorProductos = 0;
    constructor(nombre, precio){
        this._idProducto = ++Producto.contadorProductos;
        this._nombre = nombre;
        this._precio = precio;
    }

    get idProducto(){
        return this._idProducto;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get precio(){
        return this._precio;
    }

    set precio(precio){
        this._precio = precio;
    }

    toString(){
        return `
        Id Producto:${this._idProducto}, 
        Nombre: ${this._nombre},
        Precio: ${this._precio}`;
    }
}// Fin de la Clase Producto

class Orden{

    static contadorOrden = 0;

    static getMAX_PRODUCTOS(){
        return 5;
    }
    constructor(){
        this._idOrden = ++Orden.contadorOrden;
        this._productos = [];
        this._contadorProductosAgregados = 0;
    }

    get idOrden(){
        return this._idOrden;
    }

    agregarProducto(producto){
        if(this._productos.length < Orden.getMAX_PRODUCTOS()){
            this._productos.push(producto);// Tenemos 2 tipos de sintaxis: 1
            //this._productos[this._contadorProductosAgregados++] = producto;// segunda sintaxis
        }

        else{
            console.log('No se pueden Agregar mas Productos')
        }
    
    }// Fin del metodo agregar producto
    
    calcularTotal(){
        let totalVenta = 0;
        for(let producto of this._productos){
            totalVenta += producto.precio;
    
        }// Fin Ciclo For
    
        return totalVenta;
    
    }// Fin del metodo Calcular Total

    mostrarOrden(){
        let productoOrden = ' ';
        for(let producto of this._productos){
            productoOrden += producto.toString()+' ';
        }// Fin Metodo mostrar Orden
        console.log(`Orden: ${this._idOrden}, Total: ${this.calcularTotal()}, Productos: ${productoOrden}`)
    }// Fin de la clase Orden
}

let producto1 = new Producto('Mando de PS4', 40000)
let producto2 = new Producto('Cable usb tipo C', 9000)

let orden1 = new Orden();

orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.mostrarOrden();