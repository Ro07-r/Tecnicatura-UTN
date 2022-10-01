
package Ejercicio04;

import javax.swing.JOptionPane;

public class ejercicio4 {
    public static void main(String[] args) {
        int acumulador = 0;
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        while(numero >= 0){
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
            acumulador++;
        }
        JOptionPane.showMessageDialog(null, "Los numeros positivos ingresados son: " + acumulador);
}
}
