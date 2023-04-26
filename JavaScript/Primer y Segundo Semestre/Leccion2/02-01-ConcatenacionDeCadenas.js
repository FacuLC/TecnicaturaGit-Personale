var nombre = 'Facundo Leonel '
var apellido = 'Cano'

var nombreCompleto = nombre+' '+apellido // Primera Concatenacion
console.log(nombreCompleto);

var nombreCompleto2 = 'Agustina'+' '+'Pachado'; // Segunda Concatenacion
console.log(nombreCompleto2)

var juntos = nombre + 219; // Lee de izquierda a derecha siguiendo la cadena lee el numero como str
console.log(juntos);

juntos = nombre + (78 + 17) // Aqui se puede diferenciar a traves de los parentesis
console.log(juntos)

juntos = 78 + 17 +" "+nombre
console.log(juntos)

nombre += apellido // Otra manera de concatenar usando el operador simplificado
console.log(nombre)

let x, y; // Se puede crear varias variables dentro de una misma linea
x = 17, y = 21; // Se puede hacer signacion de varias variables dentro de la misma linea

let z = x + y; // Se asigna el valor de la operacion
console.log(z);

let num = 31; // No utilizar numeros para iniciar el nombre de una variable
let rompiendo = 'rompe'; // No podemos utilizar una palabra recervada para iniciar una variable
console.log(num)
console.log(rompiendo) 