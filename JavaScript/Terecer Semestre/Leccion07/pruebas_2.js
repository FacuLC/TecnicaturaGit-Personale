bienvenida = function(nombre, genero){
    genero = genero.toLowerCase()
    if(genero == 'hombre'){
        return 'Hola '+nombre+', BIENVENIDO PA'
    }
    if(genero == 'mujer'){
        return 'Hola '+nombre+', BIENVENIDA REINA'
    }
    else
    return 'ERROR EN EL INGRESO DE DATOS'
}

console.log(bienvenida('Facundo', 'hombre'));
console.log(bienvenida('Erika', 'mujer'));
console.log(bienvenida('Facundo', 'hogbt'));