package domain;

public class Persona {
    //Atributos de herencia (Modificador de acceso 'protected')
    private String nombre;
    private char genero;
    private int edad;
    private String direccion;
    
    //Creamos el constructor (Primero creamos el constructor vacio este es para crear objetos sin necesidad de inicializar los atributos de la clase.
    //Cuando creamos un constructor que necesita parametros el constructor vacio no se va a crear automaticamente por eso lo creamos nosotros).
    //El modificador de acceso en el constructor y metodos debe ser de tipo publico. 
    //Los constructores llevan el mismo nombre de la clase.
    //CADA CONSTRUCTOR QUE AGREGAMOS ES PARA PODER CREAR DISTINTOS OBJETOS DE DISTINTAS MANERAS CON VALORES INICIALES DE DISTINTA FORMA
    public Persona(){ //Constructor n°1 vacio
        
    }
    
    public Persona(String nombre){ //Constructor n°2 con parametros
        this.nombre = nombre;
    }

    public Persona(String nombre, char genero, int edad, String direccion) {
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.direccion = direccion;
    }

    public String getDireccion() {
        return this.direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public char getGenero() {
        return this.genero;
    }

    public void setGenero(char genero) {
        this.genero = genero;
    }

    public int getEdad() {
        return this.edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    @Override 
    public String toString() { //toString() es un metodo de la clase padre object
        return "Persona{" + "nombre=" + nombre + ", genero=" + genero + ", edad=" + edad + ", direccion=" + direccion + '}';
    }
    
    
    
}
