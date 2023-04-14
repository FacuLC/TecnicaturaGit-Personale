let month = 1;
switch (month) {
    case 1:
        console.log('Es Enero')
        break;
    case 2:
        console.log('Es Febrero')
        break;
    case 3:
        console.log('Es Marzo')
        break;
    case 4:
        console.log('Es Abril')
        break;
    case 5:
        console.log('Es Mayo')
        break;
    case 6:
        console.log('Es Junio')
        break;
    case 7:
        console.log('Es Julio')
        break;
    case 8:
        console.log('Es Agosto')
        break;
    case 9:
        console.log('Es Septiembre')
        break;
    case 10:
        console.log('Es Octubre')
        break;
    case 11:
        console.log('Es Noviembre')
        break;
    case 12:
        console.log('Es Diciembre')
        break;    
    default:
        console.log('Opcion Incorrecta')
        break;
}
 // Opcion Mejorada

 let month2 = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
 function getmonth(n){
    if(n < 1 || n > 12){
        throw Error('Out The Range')
    }
    return month2[n-1]
 }
 console.log(getmonth(4))