
if(genero == 'hombre'){
    return 'Hola '+nombre+', Te damos la Bienvenida Crack'
}












class Bienvenida{

    constructor(nombre, genero){
        this.nombre = nombre;
        this.genero = genero;
       genero = genero.toLowerCase();
    }

    Saludo = function(){
        if (genero == 'hombre'){
            return 'Hola '+this.nombre+', Te damos la Bienvenida Crack';
        }
        if (genero == 'mujer'){
            return 'Hola '+this.nombre+', Te damos la Bienvenida Reina';
        }
    }
    
    toString(){
        return this.Saludo
    }  
}

let persona1 = new Bienvenida('LEO', 'hombre')
console.lo