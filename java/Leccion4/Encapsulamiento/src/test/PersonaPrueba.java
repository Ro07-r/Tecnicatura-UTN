package test;
import dominio.Persona;
//Importamos la clase Persona porque está en otro paquete
public class PersonaPrueba { //Para ir testeando la clase Persona
    public static void main(String[] args) {
        Persona persona1 = new Persona("Rosalia", 120000, false); //Creacion del primer objeto
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        
    //Modificar a través de los métodos
        persona1.setNombre("Sofía"); //Cuando tenemos un encapsulamiento de tipo private trabajamos de esta manera
        //persona1.nombre = "Sofía"; //Ya no podemos utilizar esta forma de acceder a los atributos porque el acceso es privado
        //System.out.println("Nombre es: "+persona1.nombre); //ERROR
        System.out.println("persona1 su nombre modificado es: "+persona1.getNombre());
        System.out.println("persona1 su sueldo es: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        
        Persona persona2 = new Persona("Cristian", 200000, true); //Creacion del segundo objeto
        System.out.println("persona2 nombre: "+persona2.getNombre());
        System.out.println("persona2 sueldo: "+persona2.getSueldo());
        System.out.println("persona2 para obtener booleano: "+persona2.isEliminado());
        
        persona2.setNombre("Julia");
        System.out.println("persona2 con nombre modificado: "+persona2.getNombre());
        persona2.setSueldo(50000);
        System.out.println("persona2 con sueldo modificado: "+persona2.getSueldo());
        persona2.setEliminado(false);
        System.out.println("persona2 con boolean modificado: "+persona2.isEliminado());
    }
}
