package Ejercicio03;

import java.util.Scanner;

public class Ejercicio03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num;
        do{
            System.out.println("Ingrese un numero: ");
            num = Integer.parseInt(entrada.nextLine());
            if (num % 2 == 0){
                System.out.println("El numero ingresado es par");
            } else {
                if (num % 2 != 0){
                    System.out.println("El numero ingresado es impar");
                }
            }
        } while(num != 0);
        
    }
}
