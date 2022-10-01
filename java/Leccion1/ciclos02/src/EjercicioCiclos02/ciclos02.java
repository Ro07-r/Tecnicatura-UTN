package EjercicioCiclos02;
//Ejercicio 2: Leer un numero e indicar si es positivo o negativo. El proceso se va a repetir hasta que
//se introduzca un 0

import java.util.Scanner;


public class ciclos02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero; //Si yo inicializo afuera del bucle me va a reconocer la variable 'numero' por fuera del ciclo porque es global
        do{
        System.out.println("Ingrese un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        //numero= entrada.nextInt(); // La variable numero inicializada arriba tiene que estar con esta línea o con la
        //linea 'numero=Integer.parseInt(entrada.nextLine())
        if(numero > 0){
            System.out.println("El numero: " + numero + " es un numero positivo");
        } else{
            if(numero < 0){
                System.out.println("El numero: " + numero + " es un numero negativo");
            }
        } 
        }while(numero !=0);
        

            
        
        }
        }
