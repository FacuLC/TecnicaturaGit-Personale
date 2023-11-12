package Ejercicio_5;

import java.util.Scanner;

public class Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        System.out.println("Ingrese la Primera Calificacion: ");
        var cali1 = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese la segunda Calificacion: ");
        var cali2 = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese la tercera calificaion: ");
        var cali3 = Integer.parseInt(entrada.nextLine());
        var solucion = (cali1+cali2+cali3)/3;
        System.out.println("La calificaion final es = " + solucion);
        
    }
    
}
