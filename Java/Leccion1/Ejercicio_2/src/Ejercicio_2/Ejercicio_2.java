package Ejercicio_2;

import java.util.Scanner;

public class Ejercicio_2 {
    
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite sus horas semanales Trabajadas: ");
        var horaSemana = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite su Salario por hora: ");
        var salarioHora = Integer.parseInt(entrada.nextLine());
        var solucion = horaSemana * salarioHora;
        System.out.println("\nSu salario seria de = $" + solucion);
    
    }
    
}
