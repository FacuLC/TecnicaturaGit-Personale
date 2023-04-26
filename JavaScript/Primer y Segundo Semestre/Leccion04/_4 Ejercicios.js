// Evitar repetir tu codigo
// Dry don´t repeat yourself

let days = 7;

switch (days) {
    case 1:
        console.log('Hoy es Lunes')
        break;
    case 2:
        console.log('Hoy es Martes')
        break;
    case 3:
        console.log('Hoy es Miercoles')
        break;
    case 4:
        console.log('Hoy es Jueves')
        break;
    case 5:
        console.log('Hoy es Viernes')
        break;
    case 6:
        console.log('Hoy es Sabado')
        break;
    case 7:
        console.log('Hoy es Domingo')
        break;        
    default:
        console.log('Error opcion incorrecta')
        break;
}



// Esta es una Forma mas resumida y mejorada

let days2 = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];
// En la tupla de arriba empieza desde cero

function getDay(n){
    if(n < 1 || n > 7){
        throw new Error('out the range')
    }
    return days2[n-1];// Por eso ponemos (n-1) = 0
}
console.log(getDay(5))