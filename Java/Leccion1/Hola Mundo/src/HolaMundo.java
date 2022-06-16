
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
        /*char miVariableChar = 'a';
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
        System.out.println("carcterChar = " + carcterChar);*/
        //Tipos primitivos booleanos
        /*var varBool = false;
        System.out.println("varBool = " + varBool);
        
        if (varBool){
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("La bandera es roja \n");
        }
        
        //Algoritmos: ¿Es mayor de edad?
        
        var edad = 18; //Literal tiene presente la inferencia de tipos
        //var adulto = edad >= 18;//Esta es una exprecion booleana
        
        if (edad >= 18) {
            System.out.println("Es mayor de edad ");
        }
        else{
            System.out.println("Eres menor de edad");
        }*/
        //Convercion de tipos primitivos
//    var edad = Integer.parseInt("20");
//    System.out.println("edad = " + (edad + 1));
//    var valorPI = Double.parseDouble("3.1416");
//    System.out.println("valorPI = " + valorPI);
//    
//    //Pedir un valor
//      var entrada = new Scanner (System.in);
//        System.out.println("Digite su edad");
//        edad = Integer.parseInt(entrada.nextLine());
//        System.out.println("edad = " + edad );
        // Conversion de tipos primitivos en Java parte2
//    var edadTexto = String.valueOf(10);
//    System.out.println("edadTexto = " + edadTexto);
//    
//    var fraseChar = "Programadores".charAt(3);
//        System.out.println("fraseChar = " + fraseChar);
//    
//        System.out.println("Digite un caracter");
//        fraseChar = entrada.nextLine().charAt(0);
//        System.out.println("fraseChar = " + fraseChar);
//    int num1 = 5, num2 = 4;
//    var solucion = num1 + num2;
//        System.out.println("solucion suma = " + solucion);
//    solucion = num1 -num2;
//        System.out.println("solucion de la resta = " + solucion);    
//    solucion = num1 * num2;
//        System.out.println("solucion de la multiplicacion = " + solucion);
//    solucion = num1/num2;
//        System.out.println("solucion de la division = " + solucion);
//    
//    var solucion2 = 3.4 /num2;
//        System.out.println("solucion2 de la division = " + solucion2);    
//     solucion = num1 % num2; //Guarda el residuo entero de la division
//        System.out.println("solucion2 = " + solucion2);
//    
//        if (num2 % 2 == 0) 
//            System.out.println("El numero es Par");
//        else
//            System.out.println("El numero es Impar");
//    
//    int varNum1 = 1, varNum2 = 4;
//    int varNum3 = varNum1 + 6 - varNum2;
//        System.out.println("varNum3 = " + varNum3);
//    
//    varNum1 += 1; // varNum1 = varNum1 + 1;   
//        System.out.println("varNum1 = " + varNum1);
//    
//    varNum1 -=1;
//        System.out.println("varNum1 = " + varNum1);
//    
//    varNum1 *=1;
//        System.out.println("varNum1 = " + varNum1);
//    
//    varNum1 /=1;
//        System.out.println("varNum1 = " + varNum1);
//    
//    varNum1 %=1;
//        System.out.println("varNum1 = " + varNum1);
//Operadores Unarios
//    var varA = 7;
//    var varB = -varA;
//        System.out.println("varA = " + varA);
//        System.out.println("varB = " + varB+"\n"); //Resultado un numero Negativo
//        
//        //Operadores de Negacion
//        var varC = true;
//        var varD = !varC;
//        System.out.println("varC = " + varC);
//        System.out.println("varD = " + varD+"\n");
//    
//   //Operadores Unarios de Incremento
//   var varE = 9;//Se va a modificar su valor
//   var varF = ++varE;//Simbolo antes de la variable
//   //Primero incrementa la variable y despues se usa su valor
//        System.out.println("varE = " + varE);//Se incrementa su valor
//        System.out.println("varF = " + varF+"\n");//Se va a usar su valor
//    
//    //Postincremento (El simbolo va despues de la variable)
//    var varG = 3;
//    var varH = varG++;// Primero el valor de la variable, luego el incremento
//        System.out.println("varG = " + varG);
//        System.out.println("varH = " + varH+"\n");
//        
//    //Operadores unarios de decremento    
//    var varI = 4;
//    var varJ = --varI;
//        System.out.println("varI = " + varI);
//        System.out.println("varJ = " + varJ+"\n");
//    
//    //Postdecremento
//    var varK = 8;
//    var varL = varK--;
//        System.out.println("varK = " + varK);
//        System.out.println("varL = " + varL);    
//Operadores de Igualdad y Relacionales
//    var aNum = 5;
//    var bNum = 4;
//    var cNum = (aNum == bNum);
//        System.out.println("cNum = " + cNum+"\n");
//    
//    var dNum = aNum != bNum;
//        System.out.println("dNum = " + dNum+"\n");
//    
//    var cadenaA = "hello";    
//    var cadenaB = "bye bye";
//    var cVar = cadenaA == cadenaB;
//        System.out.println("cVar = " + cVar+"\n");
//    
//    var fVar = cadenaA.equals(cadenaB);
//        System.out.println("fVar = " + fVar+"\n");
//    
//    var gVar = aNum > bNum;// > >= < <= == !=
//        System.out.println("gVar = " + gVar+"\n");
//    
//        if (bNum % 2 == 0) 
//            System.out.println("El numero es par\n");
//        else
//            System.out.println("El numero es impar\n");
//        
//    var edad = 30;
//    var adulto = 18;
//        if (edad >= adulto) {
//            System.out.println("Es mayor de edad\n");
//        }
//        else {
//            System.out.println("Es menor de edad\n");
//        }
        //Opradores condicionales
//    var valorA = 7;
//    var valorMinimo = 0;
//    var valorMaximo = 10;
//    var respuesta = valorA >= 0 && valorA <= 10; // (&&) operador "and"
//     
//        if (respuesta == true) {
//            System.out.println("Esta dentro de el rango establecido\n");
//        }
//        else {
//            System.out.println("Esta fuera del rango establecido\n");
//        }
//     
//    var vacaciones = false;
//    var diaLibre = true;
//        if (vacaciones || diaLibre) {
//            System.out.println("Papa puede asistir al juego\n");
//        }
//        else{
//         System.out.println("Papa no puede asistir al juego\n");       
//        }
        //Operador Ternario
//    var resultadoT = ( 5 > 4 ) ? "Verdadero" : "Falso";
//        System.out.println("resultadoT = " + resultadoT);
//    
//        var numeroT = 7;
//        resultadoT = (numeroT % 2 == 0)? "Par": "Impar";
//        System.out.println("resultadoT = " + resultadoT);
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("z = " + z);

        var solucionAritmetica = 4 + 5 * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica);
    
        solucionAritmetica = (4 + 5) * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica);
    
    
    }

}
