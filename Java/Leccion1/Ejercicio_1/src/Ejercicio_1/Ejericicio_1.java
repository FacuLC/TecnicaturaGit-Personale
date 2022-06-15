package Ejercicio_1;

import java.util.Scanner;

public class Ejericicio_1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese su Titulo: ");
        var titulo = entrada.nextLine();
        System.out.println("Ingrese un Autor: ");
        var autor = entrada.nextLine();
        System.out.println("El Libro \""+titulo+"\" fue escrito por: "+autor);
        
        
        
    }
    
}
