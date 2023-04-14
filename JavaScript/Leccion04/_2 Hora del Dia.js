// Ejercicio calcular la hora del dia

let hora = 2;
let horario;

if(hora >= 6 && hora <= 11){
    horario = 'De la Mañana'
}
else if(hora >=12 && hora <= 14){
    horario = 'Del Mediodia'
}
else if(hora >= 15 && hora <= 19){
    horario = 'De la Tarde'
}
else if(hora >= 20 && hora <= 24){
    horario = 'De la Noche'
}
else{
    horario = 'El valor es Incorrecto'
}
console.log('Estamos en el horario de: '+horario)
