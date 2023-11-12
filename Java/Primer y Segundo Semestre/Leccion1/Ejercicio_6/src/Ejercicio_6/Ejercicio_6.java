package Ejercicio_6;

import java.util.Scanner;

public class Ejercicio_6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese la cantidad de dolares que tiene Guillermo: ");
        var dolar1 = Integer.parseInt(entrada.nextLine());
        var luis = dolar1/2;
        var juan = (dolar1+luis)/2;
        System.out.println("Guillermo tiene = UDS" +dolar1 );
        System.out.println("Luis tiene = UDS" + luis);
        System.out.println("Juan tiene = UDS" + juan);
    }
    
}
