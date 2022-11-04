
package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a; //Valor por default es 0 cuando no se inicializa una variable
    int b;
    
    //Sobrecarga de constructores(Java va a saber qué constructor tomar)
    public Aritmetica(){
        System.out.println("Se está ejecutando el constructor 1");
    }
    
    public Aritmetica(int a, int b){
        this.a = a;
        this.b = b;
        System.out.println("Se está ejecutando el constructor 2");
    }
    
    //Metodo (comienzan con el modificador de acceso)
    public void sumar(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado); //Este metodo NO retorna nada. Solo un mensaje.
    }
    
    public int sumarConRetorno(){
        //int resultado = a + b;
        return a + b; //Este metodo retorna un valor.
    }
    
    public int sumarConArgumentos(int arg1, int arg2){
        a = arg1;
        b = arg2;
        //return a + b;
        return sumarConRetorno(); //Estoy llamando un metodo dentro de otro metodo. Esto lo puedo hacer dentro de la misma clase.
    }
    
}
