//Realizar un juego para adivinar un numero. Generar un numero aleatorio entre 0-100
//Pedir numeros indicando si es "mayor" o "menor" con respecto a N.
//El proceso termina cuando el usuario acierta y mostramos el numero de intentos.
package ejercicio05;

import javax.swing.JOptionPane;

public class ejercicio05 {
        public static void main(String[] args) {
            int acumulador = 0;
            int num = 0;
            int aleatorio = (int) (Math.random() *100); //Codigo para generar un numero aleatorio en Java
            while(num != aleatorio){
                num = Integer.parseInt(JOptionPane.showInputDialog("Adivine el numero secreto. Ingrese un numero: "));
                if(num < aleatorio){
                    JOptionPane.showMessageDialog(null, "El numero secreto es mayor");
                } else if(num > aleatorio){
                    JOptionPane.showMessageDialog(null, "El numero secreto es menor");
                } else if(num == aleatorio){
                    JOptionPane.showMessageDialog(null, "¡Felicitaciones! El numero secreto es: " +aleatorio);
                }
                acumulador++;
        }            
            JOptionPane.showMessageDialog(null, "Cantidad de intentos: " +acumulador);
    }
}

   
    
 

