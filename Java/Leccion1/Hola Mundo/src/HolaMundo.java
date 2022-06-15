
import java.util.Scanner;

public class HolaMundo {

    public static void main(String[] args) { // Atajo = psvm + tab
        /* System.out.println("Hola Mundo desde Java"); // sout + tab
            int miVariable = 10;
           System.out.println(miVariable); //Atajo Ctrl + Espacio
           //Reutilizar la Variable
           miVariable = 5;
           System.out.println(miVariable);
           //Tipo String
           String miVariableCadena = "Bienvenidos"; 
           System.out.println(miVariableCadena);
           miVariableCadena = "Sigamos Creciendo en Programacion";
           System.out.println(miVariableCadena); //Ctrl + Click Izq = Origen de la Variable
         */


        // var - inferencia de tipos en java
        /* var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos Estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);

        // Reglas para definir una variable en Java
        var usuario = "Facundo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union); 
        
        var usuario2 = "Leoenel";
        var a = 8;
        var b = 4;
        System.out.println(usuario2 + " " +(a + b));
        
        // Ejercicio Caracteres Especiales con Java
        
        var nombre = "Natalia";
        System.out.println("\nNueva Linea: \n" + nombre); // el comando (\n) es un salto de linea
        System.out.println("Tabulador: \t"+nombre);
        System.out.println("\t.:MENU:."); //El comando (\t) hace un espacio en la terminal
        System.out.println("Retroseso: \b"+nombre); // Retroseso (\b) quita un espacio hacia atras
        System.out.println("Comillas Simples: \'"+nombre+"\'");
        System.out.println("Comilas Dobles: \""+nombre+"\""); */
        
        //Clase Scanner 
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su Nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el Titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);*/
        
       /* byte numEnteroByte = 127;
        System.out.println("numEnteroByte: " + numEnteroByte);
        System.out.println("Valor minimo del Byte: "+ Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte: \n"+ Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("\nnumEnteroShort: " + numEnteroShort);
        System.out.println("Valor minimo del Short: "+ Short.MIN_VALUE);
        System.out.println("Valor maximo del Short: \n"+ Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("\nnumEnteroInt: " + numEnteroInt);
        System.out.println("Valor minimo del int: "+ Integer.MIN_VALUE);
        System.out.println("Valor maximo del int: \n"+ Integer.MAX_VALUE);
        
        long numEbteroLong = 9223372036854775807L;
        System.out.println("numEbteroLong = " + numEbteroLong);
        System.out.println("Valor minimo del long: "+ Long.MIN_VALUE);
        System.out.println("Valor maximo del long: "+ Long.MAX_VALUE);*/
        
       /*float numFloat = 3.4028235E38F; 
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo de Float: "+ Float.MIN_VALUE);
        System.out.println("El valor maximo de Float: "+ Float.MAX_VALUE);
        
        double numdouble = 1.7976931348623157E308;
        System.out.println("numdouble = " + numdouble);
        System.out.println("El valor minimo de Double: "+ Double.MIN_VALUE);
        System.out.println("El valor maximo de Double: "+ Double.MAX_VALUE);*/
        
        // Inferencia de tipos var y tipos primitivos
        /*var numeroEntero = 20; //Las literales sin punto se quedan como tipo int
        System.out.println("numeroEntero = " + numeroEntero);    
        var numFloat = 10.0F; //Se tranforma en tipo Double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);*/
        
        //Tipos Primitivos char
        
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
     
        char varCaracter = '\u0024'; // Indicamos a java la asignacion con el valopr unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCarcterDecicmal = 36; //valoe decimal del juego de carcter unicode
        System.out.println("varCarcterDecicmal = " + varCarcterDecicmal);
        char varCarcterSimbolo = '$'; //Un carcter especial
        System.out.println("varCarcterSimbolo = " + varCarcterSimbolo + "\n");
        
        var varCaracter1 = '\u0024'; // Indicamos a java la asignacion con el valopr unicode
        System.out.println("varCaracter = " + varCaracter);
        var varCarcterDecicmal1 = (char)36; //valoe decimal del juego de carcter unicode
        System.out.println("varCarcterDecicmal = " + varCarcterDecicmal);
        var varCarcterSimbolo1 = '$'; //Un carcter especial
        System.out.println("varCarcterSimbolo = " + varCarcterSimbolo+ "\n");
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int carcterChar = 'b';
        System.out.println("carcterChar = " + carcterChar);
        
        
        
    }
    
}
