//5. - Muestre la suma de los números impares del 1 al 100
let numero4 = 1;
let suma1 = 0;
while(numero4 < 100){
    if(numero4 % 2 !==0){
        suma1 += numero4;
        numero4 += 1;
    }
    console.log(suma1)
}
console.log('Fin del Programa')



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

    toString(){ nombreCompleto = this._nombre+' '+this._apellido // Regresa un String
        return this.nombreCompleto();
    }

}

console.log(persona1.nombreCompleto);