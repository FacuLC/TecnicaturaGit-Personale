package main.de.segundo.semestre;

public class MainDeSegundoSemestre {

    public static void main(String[] args) {
        var conteo = 0; //Inferencia de tipos
        while (conteo <= 7){
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en uno las variables
        }
        var contador = 0;
        do {            
            System.out.println("contador = " + contador);
            contador++;
        } while (contador <=7);
        
        for(var contando =0; contando < 7; contando++ ){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
            }
        }
        for(var contando =0; contando < 7; contando++ ){
            if(contando % 2 != 0){
                continue; //Vamos a la siguiente iteracion;
            }
                System.out.println("contando = " + contando);
        }
    }
    
}
