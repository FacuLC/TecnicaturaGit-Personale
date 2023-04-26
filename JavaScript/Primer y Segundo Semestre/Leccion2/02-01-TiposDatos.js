
//Tipo String
var nombre = 'Facundo'
console.log(nombre)

//Tipo Numerico
var numero = 3000 //Tipo Numerico
console.log(numero)

//Tipo Objeto
var objeto = {
    nombre : 'Facundo',
    apellido : 'Cano',
    telefono : '2974603992'
}

console.log(objeto)


//CLASE - 4

//Tipo de dato Booelan
var bandera = true
console.log(bandera)

//Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion) 

//Tipo de dato symbol
var simbolo = Symbol('Mi simbolo')
console.log (simbolo)

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre
        this.apellido = apellido
    }
}

console.log(Persona)

// CLASE - 5

// Tipo de dato undeffined
var x
console.log(typeof x)

x = undefined
console.log(typeof x)

// null: significa ausencia de valor
var y = null; //null no es un tipo de dato, pero su origen es un object
console.log(typeof y)

// Tipo de dato array y Empty String
var autos = ['Citroen', 'Audi', 'BMW', 'Ford']
console.log(autos)
console.log(typeof autos) // Preguntamos que tipo de dato es:

var z = '';
console.log(z); // Esto se refiere a que la cadena esta vacia
console.log(typeof z);