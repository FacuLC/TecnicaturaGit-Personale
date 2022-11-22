var nombre = 'Leonel '
var apellido = 'Cano'
var nombreCompleto = nombre+' '+apellido // Primera Concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = 'Nicoel'+' '+'Flores'; // Segunda Concatenacion
console.log(nombreCompleto2)
var juntos = nombre + 219; // Lee de izquierda a derecha siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + (78 + 17) // Aqui se puede diferenciar a traves de los parentesis
console.log(juntos)
juntos = 78 + 17 + nombre
console.log(juntos)

nombre += apellido
console.log(nombre)