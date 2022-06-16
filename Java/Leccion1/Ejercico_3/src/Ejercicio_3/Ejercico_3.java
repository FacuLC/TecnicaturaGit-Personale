package Ejercicio_3;

import java.util.Scanner;

public class Ejercico_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        System.out.println("Ingrese la altura de el rectangulo: ");
        var altura = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el ancho de el rectangulo: ");
        var ancho = Integer.parseInt(entrada.nextLine());
        
        var area = ancho * altura;
        System.out.println("El Area de el rectangulo es = " + area);        
        var perimetro = (ancho + altura)*2;
        System.out.println("El Perimetro de el rectangulo es = " + perimetro);
    }
}
