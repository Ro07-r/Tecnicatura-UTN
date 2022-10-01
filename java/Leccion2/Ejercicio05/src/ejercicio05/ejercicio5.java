//Realizar un juego para adivinar un numero. Generar un numero aleatorio entre 0-100
//Pedir numeros indicando si es "mayor" o "menor" con respecto a N.
//El proceso termina cuando el usuario acierta y mostramos el numero de intentos.
//CLASE SCANNER
package ejercicio05;

import java.util.Scanner;

public class ejercicio5 {
    public static void main(String[] args) {
        int acumulador = 0;
        Scanner practica = new Scanner(System.in);
        int aleatorio = (int) (Math.random() *100);
        int num = ' ';
        while(num != aleatorio){
            System.out.println("Adivine el número secreto: ");
            num= practica.nextInt();
            if(num < aleatorio){
                System.out.println("El numero secreto es mayor");
        } else if(num > aleatorio){
            System.out.println("El numero secreto es menor");
        } else if(num == aleatorio){
            System.out.println("¡Felicitaciones! El numero secreto es: " + aleatorio);
        }
            acumulador++;            
        }
        System.out.println("Cantidad de intentos: " + acumulador);        
    }
}
