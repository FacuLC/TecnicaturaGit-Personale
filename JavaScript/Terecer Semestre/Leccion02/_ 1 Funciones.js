miFuncion(8, 8);//Esto se lo conoce como hosting

function miFuncion(a, b){
    //console.log('Sumamos: '+ (a + b)); // De esta forma la funcion por si sola ejecuta el (return) 
    return a + b;
}

// LLamamos a la Funcion
miFuncion(12, 12);

let resultado = miFuncion(6, 7);
console.log(resultado)


// Funciones de tipo Exprecion
let x = function(a, b){return a + b};// Necesita cierre con punto y coma
resultado = x(3, 12);// Al llamarla se pone la variable y parentesis
console.log(resultado);


// Funciones de tipo (self y invoking) que se llaman a si mismas 
(function(a, b){
    console.log('Ejecutando la Funcion: '+ (a + b))
})(9, 6);// NO podemos volver a utilizar mas de una vez la funcion

console.log(typeof miFuncion);


// Para saber cuantos argumetos tiene nuestra funcion
function miFuncion2(a, b){
    console.log(arguments);
}
miFuncion2(5, 7, 3, 6, 8)


// toString
var miFuncionTexto = miFuncion2.toString();// Ejecutamos la funcion en modo de texto
console.log(miFuncionTexto);



//Funciones Tipo Flecha
//no usar palabra reservada (function), tampoco ( {'llaves'} ) y ( return )
//en esta funcion se usa ( '=>' ) en modo de flecha 
const sumarFuncionFlecha = (a, b) => a + b;//Podemos Asignar el resultado a una variable o podemos abreviar
console.log(sumarFuncionFlecha(3,8));


let sumar = function(a, b){
    console.log(arguments[0]);// Muestra el parametro de 'a'
    console.log(arguments[1])
    console.log(arguments[2])
    return a + b + arguments[2]
}
console.log(sumar(3, 35, 53))


//Sumar todo los Argumentos
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i];// arguments: es para arreglos
    }
    return suma;
}


// Consepto Hoisting

let resultado2 = sumarTodo2(3, 4, 45, 643, 63);
console.log(resultado2);
function sumarTodo2(){
    let suma2 = 0;
    for(let i = 0; i < arguments.length; i++){
        suma2 += arguments[i];
    }
    return suma2
}


// Paso valor
//Tipo primitivos

let y = 10;
function cambiarValor(a){
    a = 20;
}

cambiarValor(y);
console.log(y);


