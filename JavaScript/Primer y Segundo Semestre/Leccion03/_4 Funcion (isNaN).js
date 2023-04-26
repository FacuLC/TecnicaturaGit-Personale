// Funcion isNaN
let miNumero = '20';// Es una Cadena
console.log(typeof miNumero);

let edad = Number(miNumero);// Esta es mi funcion
console.log(typeof edad);

if(isNaN(edad)){ // isNaN = no es un numero / is Not a Number (Devuelve un resultado booleano)
    console.log('La Variable no es solo numeros')
}
else{
    if(edad >= 18){
        console.log('Puede Votar porque es mayor de edad')
    }
    else{
        console.log('Es demasiado joven para poder votar')
    }
}