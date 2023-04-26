//5. - Muestre la suma de los números impares del 1 al 100
let numero4 = 1;
let suma1 = 0;
while(numero4 < 100){
    if(numero4 % 2 !==0){
        suma1 += numero4;
        numero4 += 1;
    }
    console.log(suma1)
}
console.log('Fin del Programa')
