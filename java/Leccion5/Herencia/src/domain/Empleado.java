package domain;

public class Empleado extends Persona{ //La clase Empleado hereda de la clase Persona
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados; //Para incrementar
    
    //Constructor
    public Empleado(String nombre, double sueldo) {
        super(nombre); //Porque estamos utilizando un atributo que viene de la clase padre
        this.idEmpleado = ++Empleado.contadorEmpleados; //Aumento para el atributo idEmpleado
        this.sueldo = sueldo;
    }

    public int getIdEmpleado() {
        return this.idEmpleado;
    }

    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder(); //StringBuilder es mas eficiente que la concatenacion con suma 
        sb.append("Empleado{idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(", ").append(super.toString()); //SIRVE PARA TRAER LOS ATRIBUTOS DE LA CLASE PADRE 'PERSONA'  
        sb.append('}');
        return sb.toString();
    }    
}
