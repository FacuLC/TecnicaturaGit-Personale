bienvenida = function(nombre, genero){
    genero = genero.toLowerCase()
    if(genero == 'hombre'){
        return 'Hola '+nombre+', Bienvenido Craken'
    }
    if(genero == 'mujer'){
        return 'Hola '+nombre+', Bienvenido Reina'
    }
    else
    return 'ERROR AL INGRESAR LOS DATOS'    
}

console.log(bienvenida('Renzo Silveira', 'hombre'));
console.log(bienvenida('Bianca Gonsalez', 'mujer'));
console.log(bienvenida('Facundo', 'hogbt'));