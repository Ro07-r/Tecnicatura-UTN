
package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a; //Valor por default es 0 cuando no se inicializa una variable
    int b;
    
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
