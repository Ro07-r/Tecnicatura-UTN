package ciclos01;
//Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir el proceso hasta que se introduzca un numero negativo
import java.util.Scanner;


public class ciclos01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Ingrese un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero > 0){
            var cuadrado = Math.pow(numero,2);            
            System.out.println("El numero: "  +  numero  +  " elevado al cuadrado es: "   +  cuadrado);
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
           }
        System.out.println("El programa ha finalizado porque ha ingresado un numero negativo");
    }        
}
