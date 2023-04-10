// Ampliamos el uso de let y const
/* 
Con 'var' puedes reasignar en cualquier momento
este forma parte del ambito global
Un error es que se sobre escriba
*/

var nombre = 'Leonel'
nombre = 'Carlos'
console.log(nombre)

function saludar(){
    var nombre = 'Esteban'
    console.log(nombre)
}
console.log(nombre) // El problema es que aqui no lee el dato de la funcion;

// Otro Ejemplo

if(true){
    var edad = 21
    console.log(edad)
}
console.log(edad) // En la funcion funciono correctamente en cambio en la estructura if fallo;

/*
let: puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloques,
solo disponible dentro de un bloque de llaves
o dentro de una funcion
*/

function saluda2(){
    let segNombre = 'Facundo'
    console.log(segNombre)
}
console.log(segNombre)

if(true){
    let edad2 = 22
    console.log(edad2)
}
console.log(edad2)

/*
const: Se utiliza para valores que no se pueden reasignar
*/

const fechaNacimiento = 20001
console.log(fechaNacimiento)

fechaNacimiento = 737642
console.log(fechaNacimiento)