package dominio;

public class Persona {
    //Atributos
    private String nombre;
    private float sueldo;
    private boolean eliminado;
    
    //Creamos el constructor de esta clase Persona. Siempre el constructor debe llevar el mismo nombre que la clase.
    public Persona(String nombre, float sueldo, boolean eliminado){ //En este caso el constructor tiene que ser de acceso publico para poder acceder a los atributos que son privados
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }
    
    //Getters and Setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public float getSueldo() {
        return sueldo;
    }

    public void setSueldo(float sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() { //Cuando es un booleano en lugar de 'get' se coloca 'is'
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
}
