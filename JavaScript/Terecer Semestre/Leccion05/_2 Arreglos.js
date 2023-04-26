
// Arreglos [Sintaxis Vieja]
// let autos = new Array('Ferrari', 'Renault', 'BMW');



// Creacion de Array o Arreglos


//Arreglo [Sintaxis Actual]
const autos = ['Ferrari', 'Renault', 'BMW'];//Se utiliza Corchetes para los arreglos

console.log(autos)

// Recordemos los elementos de un arreglo

console.log(autos[0]);
console.log(autos[2])


// Para Recorrer un arreglo

for(let i = 0; i < autos.length; i++){
    console.log(i +' : '+autos[i]);
}

// ---------------------


// Modificamos los Elementos de un Arreglo
autos[1] = 'Ford';
console.log(autos[1]);


// ---------------------


// Agregar nuevos valores al arreglo
autos.push('Audi'); // Agregamos el elemento al final del arreglo

console.log(autos);


// Otras formas de agregar elementos al arreglo
autos[autos.length] = 'Toyota';// con (. length agregamos el elemento al final)
console.log(autos);

// Trecera forma de agregar elementos teniendo cuidado
autos[6] = 'Renault';
console.log(autos);


// ------------------------

// Como preguntar si es un Array o Arreglo

// 1ra Forma
console.log(Array.isArray(autos));// Devuelve un booleano

// 2da Forma
console.log(autos instanceof Array);// Preguntamos si la variable es una instancia de la clase Array