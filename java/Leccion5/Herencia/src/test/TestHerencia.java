package test;

import domain.Cliente; //Importamos las clases Cliente y Empleado porque están fuera del package 'test'
import domain.Empleado;
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Rosalia", 57000.00); 
        System.out.println("empleado1 = " + empleado1);
        
        Cliente cliente1 = new Cliente (new Date(), true, "Cristian", 'M', 50, "Alvarez Jonte 351");
        System.out.println("cliente1 = " + cliente1);
        
        Cliente cliente2 = new Cliente (new Date(), false, "Sofia", 'F', 8, "Alvarez Jonte 351");
        System.out.println("cliente2 = " + cliente2);
    }
}
