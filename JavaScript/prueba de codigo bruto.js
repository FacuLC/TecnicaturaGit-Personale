//5. - Muestre la suma de los números impares del 1 al 100
class Persona{// Clase Padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    nombreCompleto(){
        return this._nombre+' '+this._apellido;
    }

    toString(){  
        return this.nombreCompleto();
    }

}
let persona1 = new Persona('leo','cazon');
console.log(persona1.toString());