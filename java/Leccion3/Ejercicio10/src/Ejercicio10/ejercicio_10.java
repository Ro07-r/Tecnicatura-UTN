//Ejercicio 10:
//Pedir 10 números y escribir la suma total
//Clase Scanner y JOptionPale
package Ejercicio10;

import java.util.Scanner;

public class ejercicio_10 {
    public static void main(String[] args) {
        Scanner practica = new Scanner(System.in);
        int suma = 0, i = 0;
        while (i < 10){
            System.out.println("Digite un número: ");
            int numero = practica.nextInt();
            suma += numero;
            i ++;
        }  
        System.out.println("La suma de los 10 numeros ingresados es: " + suma);
    }   
}

