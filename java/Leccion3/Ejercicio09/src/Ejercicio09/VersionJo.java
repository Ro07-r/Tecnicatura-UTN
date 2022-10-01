//Pedir el día, mes y año de una fecha e indicar si la fecha es correcta.
//Clase Scanner y Clase JOoptionPane
package Ejercicio09;

import javax.swing.JOptionPane;

public class VersionJo {
    public static void main(String[] args) {
        int dia = ' ', mes = ' ', anio = ' ';
        dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un dia de una fecha: "));
        mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un mes de una fecha: "));
        anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un año de una fecha: "));
        if(dia == 20 & mes == 8 & anio == 1972){
            JOptionPane.showMessageDialog(null, "La fecha ingresada es correcta");
        } else {
            JOptionPane.showMessageDialog(null, "La fecha ingresada no es la correcta");
        }
    }
}
