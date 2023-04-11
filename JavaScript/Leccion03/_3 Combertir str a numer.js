// Como convertir string a number
let miNumero = '20';// Es una Cadena
console.log(typeof miNumero);

let edad = Number(miNumero);// Esta es mi funcion
console.log(typeof edad);

if(edad >= 18){
    console.log('Puede Votar porque es mayor de edad')
}
else{
    console.log('Es demasiado joven para poder votar')
}

// Modo Ternario
let resultado = edad >= 18 ? 'Puede Votar porque es mayor de edad' : 'No puede Votar porque es menor de edad';
console.log(resultado)