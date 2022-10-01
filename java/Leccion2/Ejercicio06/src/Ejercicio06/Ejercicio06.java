//Pedir numeros hasta que se teclee un 0, mostrar la suma 
//de todos los numeros introducidos
//Version JOption
package Ejercicio06;
import javax.swing.JOptionPane;
public class Ejercicio06 {
    public static void main(String[] args) {
        int num, suma = 0;
        do{
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
            suma = suma + num;
        } while(num != 0);
        JOptionPane.showMessageDialog(null, "La suma de todos los numeros introducidos es: " + suma);
    }
}
