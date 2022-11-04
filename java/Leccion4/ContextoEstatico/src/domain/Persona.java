
package domain;

public class Persona {
    //Cargamos los atributos
    private int idPersona;
    private static int contadorPersona;
    private String nombre;
    
    //Constructor
    public Persona(String nombre){
        this.nombre = nombre;
        //Incrementar el contador por cada objeto nuevo
        Persona.contadorPersona++; //No se utiliza el operador this para un atributo estatico sino que se va a utilizar el mismo nombre de la clase
        //Vamos a asignar un nuevo valor a la variable idPersona
        this.idPersona = Persona.contadorPersona;        
    }
    
    public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int aContadorPersona) {
        contadorPersona = aContadorPersona;
    }

    public int getIdPersona() {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    //Creamos el metodo toString
    @Override //La notacion override agrega informacion extra al metodo que estamos definiendo que es el metodo toString. 
              //Primero la anotacion luego el metodo. La anotacion esta indicando que estamos sobreescribiendo al metodo toString.
              //Sobreescribir significa que en la herencia desde la clase object se hereda este metodo toString.
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
    
    
    
}
