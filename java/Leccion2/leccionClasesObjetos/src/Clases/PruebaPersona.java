//Constructor <- espacio de memoria
//Public <- modificador de acceso
//Int <- tipo de retorno
//Void <- tipo de retorno vacío
//This <- se crea de manera automatica. Al momento en que se ejecuta un objeto es cuando se crea esta variable.
//Apunta al objeto en ejecucion (al espacio de memoria) donde esta cargado o grabado el objeto para hacer modificaciones.
package Clases;


public class PruebaPersona {
    public static void main(String[] args) { //main para ejecutar el programa. El metodo main se recomienda crearlo fuera de la clase.
        Persona persona1; //Definimos una variable de tipo persona
        persona1 = new Persona(); //Llamamos al constructor
        persona1.nombre = "Rosalía";
        persona1.apellido = "Lotierzo";
        //Llamamos al metodo
        persona1.obtenerInformacion(); //Muestra la informacion de los valores de los atributos en la clase
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2); //Esto imprime el numero que se le ha asignado en la memoria
        persona2.obtenerInformacion(); //Al no cargar ningun valor nos da un valor por default "null"
        persona2.nombre = "Cristian";
        persona2.apellido = "Garcia";
        persona2.obtenerInformacion();
    }
}
