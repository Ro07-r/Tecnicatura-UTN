//Paso por referencia: para acceder al objeto y a la clase, el paso por referencia va a ser
//a través de la clase 'Persona'
package pasoporreferencia;

import Clases.Persona;


public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Ester"; //Al principio nos arroja error porque el atributo nombre dentro de la clase Persona no es de acceso público
        System.out.println("persona1 nombre = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio que hicimos en el nombre es: "+persona1.nombre);
        persona1 = cambiarElValor(persona1); //Pasamos el objeto persona1
        Persona persona2 = null;
        //Persona persona2 = new Persona();
        persona2 = cambiarElValor(persona2);
        //System.out.println("El nuevo valor del objeto es: "+persona2.nombre);
        
    }
    
    public static void cambiarValor(Persona persona){ //Paso por referencia
        persona.nombre = "María de Buenos Aires";
    }
    
    public static Persona cambiarElValor(Persona persona){ //Metodo de tipo objeto
        if(persona == null){
            System.out.println("Valor de persona es invalido : Null");
            return null;
        }
        else {
            persona.nombre = "Monica";
            return persona;
        }
    }
}
