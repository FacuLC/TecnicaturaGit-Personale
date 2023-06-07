let resultado = sumar_Todo(3, 5, 2, 6, 7);
console.log(resultado)
function sumar_Todo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
    suma += arguments[i];
    }
    return suma 

}

let suma = function(a, b, c){
    let rta = 0;
    if((a,b > c)){
        return rta = (a+b)/c
    
    }if((a,b)< c){
        return rta = (a+b)*c
    }
    else{
        return 'Error, no se pudo realizar la operacion'
    }
    
}
console.log(suma(3, 5, 8))



function bienvenida(nombre, sexo) {
    sexo = sexo.toLowerCase()
    if(sexo == 'hombre'){
        return 'Hola '+nombre+' Eres un Crack'
    }   
    if(sexo == 'mujer'){
        return 'Hola '+nombre+' Te deseamos una hermosa experiencia'
    }
    else{
        return 'OPCION INCORRECTA'
    }
}
console.log(bienvenida('Facundo', 'HOMBRE'))
console.log(bienvenida('Sol', 'MujEr'))
console.log(bienvenida('Facundo', 'bi nario'))