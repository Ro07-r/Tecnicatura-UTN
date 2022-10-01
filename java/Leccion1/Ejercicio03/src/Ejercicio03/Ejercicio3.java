
package Ejercicio03;

import javax.swing.JOptionPane;


public class Ejercicio3 {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero!=0){
            if(numero %2 == 0){
                JOptionPane.showMessageDialog(null, "El numero ingresado es par");
            } else {
                JOptionPane.showMessageDialog(null, "El numero ingresado es impar");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero "+numero+" finaliza el programa");
    }
}
