
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
    }
}
