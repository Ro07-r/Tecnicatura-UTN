package caja;

public class Caja {
    //Atributos (caracteristicas)
    int ancho;
    int alto;
    int profundo;
    //Metodos y constructores (acciones)
    public Caja(){ //Constructor1 está vacío, porque si creamos el contructor
        //para recibir los argumentos, el constructor vacio por defecto ya no se va a crear
    }
    //Constructor con parámetros
    public Caja(int ancho, int alto, int profundo){ //Constructor2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    public int calcularVolumen(){ //Método para calcular
        return ancho * alto * profundo;       
    }
}

