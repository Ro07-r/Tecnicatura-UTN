//TODAS LAS CLASES SON HERENCIA DE UNA CLASE OBJECT

package Operaciones;


public class PruebaAritmetica {
    public static void main(String[] args) {
        Aritmetica aritmetica1 = new Aritmetica(); //Creamos un objeto
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumar(); //El metodo sumar suma los dos valores y muestra el resultado
    
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado usando argumentos = " + resultado);
    
        System.out.println("aritmetica1 a: " +aritmetica1.a);
        System.out.println("aritmetica1 b: " +aritmetica1.b);
        Persona persona = new Persona("Ariel", "Betancud");
        System.out.println("persona = " + persona);
        System.out.println("persona nombre = " + persona.nombre);
        System.out.println("persona apellido = " + persona.apellido);
    }
}

class Persona{ //Creamos otra clase dentro de la misma plantilla. 
               //El modificador de acceso no se lo ponemos, no es necesario escribirlo porque se asigna por default. 
               //Solo puede haber una clase de tipo publica.
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){
        super(); //Llamada al constructor de la clase Padre object
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this); //Muestra el numero de referencia al espacio de memoria que se está creando
    }
}

class Imprimir{
    public Imprimir(){
        super(); //El constructor de la clase padre, para reservar memoria
    }
    
    
    public void imprimir (Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresión del objeto actual (this): "+this);
    }
    
}
