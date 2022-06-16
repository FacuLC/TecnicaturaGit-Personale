package Ejercicio_7;

import java.util.Scanner;

public class Ejercicio_7 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        final int salario = 1000;
        int comision = 150, venta;
        float salarioMes, ventaCarro, porVenta, totalPrecio;
        System.out.println("Digite la cantidad de autos vendidos: ");
        venta = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio de un carro: ");
        ventaCarro = Float.parseFloat(entrada.nextLine());
        
        comision *=venta;
        totalPrecio = ventaCarro* venta;
        porVenta= totalPrecio*0.05f;
        salarioMes = salario + comision+ porVenta;
        System.out.println("nEl salario mensual es: "+ salarioMes);
    }
    
}
