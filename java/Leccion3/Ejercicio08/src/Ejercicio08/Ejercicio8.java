//Pedir un numero N, y mostrar todos los numeros del 1 al N.
//Clase Scanner y Clase JOoptionPane
package Ejercicio08;

import java.util.Scanner;

public class Ejercicio8 {
    public static void main(String[] args) {
        Scanner practica = new Scanner(System.in);
        System.out.println("Ingrese un numero: ");
        var num= practica.nextInt();
        for(int i = 1; i <= num; i++){
            System.out.println(i);
        }
    }
}
