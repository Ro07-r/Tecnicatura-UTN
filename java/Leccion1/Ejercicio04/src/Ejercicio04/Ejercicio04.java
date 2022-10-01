package Ejercicio04;

import java.util.Scanner;


public class Ejercicio04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num;        
        int acumulador = 0;
        System.out.println("Ingrese un numero: ");
        num = Integer.parseInt(entrada.nextLine());
        while(num >= 0){
            System.out.println("Ingrese un numero: ");
            num = Integer.parseInt(entrada.nextLine());            
            acumulador++;            
        }
        System.out.println("Los numeros positivos ingresados son: " + acumulador);
    }
}
