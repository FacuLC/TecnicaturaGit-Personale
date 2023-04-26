//1.- Muestre los primeros 100 números enteros iniciando desde el 1

let numero = 0;
while(numero <= 100){
    console.log(numero)
    numero++;
}
console.log('Fin del Programa')

//2.- Muestre los primeros 100 números de forma inversa, es decir, del 100 al 1

let numero1 = 100;
while(numero1 => 0){
    console.log(numero1)
    numero1++;
}
console.log('Fin del Programa')

//3.- Muestre únicamente, los números pares en el rango del 1 al 100

let numero2 = 100;
while(numero2 % 2 == 0){
    console.log(numero2)
}
console.log('Fin del Programa')

//4. - Muestre la suma de los números del 1 al 100

let numero3 = 1;
let suma = 0;
while(numero3 <= 100){
    suma += numero3;
    numero3 += 1;
    console.log(numero3)
}
console.log('Fin del Programa')

//5. - Muestre la suma de los números impares del 1 al 100
let numero4 = 100;
while(numero4 % 2 != 0){
    console.log(numero4)
}
console.log('Fin del Programa')
