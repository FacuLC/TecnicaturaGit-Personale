package Ejercicio_4;

import java.util.Scanner;

public class Ejercicio_4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        System.out.println("Ingrese un numero: ");
        var num1 = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese otro numero: ");
        var num2 = Integer.parseInt(entrada.nextLine());
        var solucion = (num1 > num2) ? "El mayor es: " + num1 + "\nEl menor es: "+num2 : "El mayor es: "+ num2 + "\nEl menor es: "+num1;
        System.out.println(solucion);
    }
}
