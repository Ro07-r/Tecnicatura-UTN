package domain;
	
import java.util.Date; //Importamos este paquete que incluye Java para poder trabajar con fechas y horarios

public class Cliente extends Persona{

    private int idCliente;
    private boolean vip;
    private static int contadorClientes; //Para incrementar    
    private Date fecha = new Date(); //Para crear una fecha, debemos crear un objeto de esta clase
    
    //Constructor    
    public Cliente(Date fecha, boolean vip, String nombre, char genero, int edad, String direccion) {
        super(nombre, genero, edad, direccion); //Se coloca en primer lugar
        this.idCliente = ++Cliente.contadorClientes; //Aumento para el atributo idEmpleado          
        this.fecha = fecha;
        this.vip = vip;
    }

    public Date getFecha() {
        return this.fecha;
    }

    public void setFecha(Date fecha) {
        this.fecha = fecha;
    }

    public int getIdCliente() {
        return this.idCliente;
    }

    public boolean isVip() {
        return this.vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente{idCliente=").append(idCliente);
        sb.append(", vip=").append(vip);
        sb.append(", fecha=").append(fecha);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
    
    
    
}
