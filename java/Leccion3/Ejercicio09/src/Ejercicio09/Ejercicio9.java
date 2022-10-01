//Pedir el día, mes y año de una fecha e indicar si la fecha es correcta.
//Clase Scanner y Clase JOoptionPane
package Ejercicio09;

import java.util.Scanner;

public class Ejercicio9 {
    public static void main(String[] args) {
        int dia = ' ' , mes = ' ', anio = ' ';
        Scanner practica = new Scanner(System.in);
            System.out.println("Ingrese un día de una fecha: ");
            dia = practica.nextInt();
            System.out.println("Ingrese un mes de una fecha: ");
            mes = practica.nextInt();
            System.out.println("Ingrese un año de una fecha: ");
            anio = practica.nextInt();
            if(dia == 25 & mes == 1 & anio == 2014){
                System.out.println("La fecha ingresada es correcta");
            } else {
                System.out.println("La fecha ingresada no es la correcta");
            }
    }

}
