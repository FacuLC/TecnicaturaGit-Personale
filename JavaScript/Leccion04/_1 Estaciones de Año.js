//Ejerccio Calcular Estacion del Año

let mes = 12;
let estacion;

if(mes == 12 || mes == 1 || mes == 2){
    estacion = 'Estamos en Verano';
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = 'Estamos en Otoño'
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = 'Estamos en Invierno'
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = 'Estamos en Primavera'
}
else{
    estacion = 'Digitaste un valor Incorrecto'
}
console.log('El valor deice que: '+estacion)