package Ejercicio_1;

import java.util.Scanner;

public class Ejericicio_1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese su Titulo: ");
        var titulo = entrada.nextLine();
        System.out.println("Ingrese el ID de el libro: ");
        var ID = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese un Autor: ");
        var autor = entrada.nextLine();
        System.out.println("Digite el precio de el libro: ");
        var precio = Integer.parseInt(entrada.nextLine());
        System.out.println("El Libro: "+titulo+"\nAutor: "+autor+"\nID: "+ID);
        
        if (precio>=800) {
            System.out.println("El Envio de el Libro es Gratis!!");
        }
        else{
            System.out.println("El envio de el Libro es de 500$ ");
        }    
    }
    
}
