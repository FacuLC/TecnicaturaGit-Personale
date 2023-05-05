let x = 10; // Variable de tipo primitiva
console.log(x.length)


//Objeto -- De esta manera nos permite acceder a mas opciones a la hora de ser llamada 
let persona = {
    nombre: 'Facundo',
    segundoNombre: 'Leonel',
    apellido: 'Cano',
    edad: 22,
    altura: 1.78,
    email: 'facundocano79@gmail.com',
    nombreCompleto: function(){ // metodo o funcion en JavaScript
        return this.nombre+' '+this.segundoNombre+' '+this.apellido;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.edad);
console.log(persona.altura);
console.log(persona.email);
// o de esta manera
console.log(persona.nombreCompleto());


// Diferentes formas de crear objetos

let persona2 = new Object(); // Debe Crear un nuevo objeto en memoria
persona2.nombre = 'Santiago';
persona2.direccion = 'Br Guemeez';
persona2.telefono = '2414251525';
console.log(persona2.telefono);

//Accedemos como si fuera un Arreglo
console.log(persona['apellido']);

//for in
// como acceder a la propiedad y luego a su valor
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}


//Agregar y eliminar propiedades de un Objeto
persona.apellidos = 'Perez';// Cambiamos dinamicamnete un valor del objeto
delete persona.apellidos
console.log(persona);


// Distintas Formas de Imprimir un Objeto
// Numero 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log('Distintas formas de imprimir un Objeto = Forma 1')
console.log(persona.nombre+' '+persona.apellido);

//Numero 2: A traves de un Ciclo for in
console.log('Distintas formas de imprimir un Objeto = Forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Numero 3: La funcion Objet.values()
console.log('Distintas formas de imprimir un Objeto = Forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4: Utilizamos el metodo JSON.stringify
console.log('Distintas formas de imprimir un Objeto = Forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString)