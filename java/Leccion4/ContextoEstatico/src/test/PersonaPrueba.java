package test;

import domain.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Rosalia");
        System.out.println("persona1 = " + persona1); //No nos va a mostrar el valor hexadecimal para la memoria porque ya hemos cargado el metodo toString,
                                                      //pero sí va a mostrar los valores que tienen los atributos a traves del toString.
        Persona persona2 = new Persona("Sofia");
        System.out.println("persona2 = " + persona2);
    }
}
