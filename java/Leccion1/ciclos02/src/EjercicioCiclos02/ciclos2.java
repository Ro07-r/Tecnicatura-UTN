//Ejercicio 2: Leer un numero e indicar si es positivo o negativo. El proceso se va a repetir hasta que
//se introduzca un 0
//Version con JOptionPane
package EjercicioCiclos02;
import javax.swing.JOptionPane;
public class ciclos2 {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: ")); //La clase JOptionPane recibe un tipo String
                                                                                          //Por eso hay que hacer la conversion
        while(numero !=0){
           if(numero > 0){
               JOptionPane.showMessageDialog(null, "El numero: " + numero + " es un numero positivo"); //Muestra un mensaje en la ventana emergente
           } else {
               JOptionPane.showMessageDialog(null, "El numero: " + numero + " es un numero positivo"); //Muestra un mensaje en la ventana emergente
               }
           numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: ")); //Indica que ingresemos un dato 
           }
        JOptionPane.showMessageDialog(null, "El numero "+numero+" finaliza el programa");
       }
    }
       

