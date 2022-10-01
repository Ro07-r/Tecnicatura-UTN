//Pedir numeros hasta que se teclee un 0, mostrar la suma 
//de todos los numeros introducidos
//Version Scanner
package Ejercicio06;

import java.util.Scanner;

public class ejercicio6 {
    public static void main(String[] args) {
        int suma = 0;
        int acumulador = 0;
        int num = ' ';
        while(num != 0){
            Scanner practica = new Scanner(System.in);
            System.out.println("Ingrese un numero: ");
            num= practica.nextInt();
            suma = suma + num;
            acumulador++;            
        }
        System.out.println("La suma de los numeros ingresados es: " + suma);        
    }
}
