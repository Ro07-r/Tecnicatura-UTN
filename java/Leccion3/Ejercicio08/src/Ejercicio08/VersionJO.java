//Pedir un numero N, y mostrar todos los numeros del 1 al N.
//Clase Scanner y Clase JOoptionPane
package Ejercicio08;

import javax.swing.JOptionPane;


public class VersionJO {
    public static void main(String[] args) {
        int num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        for(int i = 1; i <= num; i++){
            JOptionPane.showMessageDialog(null, i);
        }
    }
}
