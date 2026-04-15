package Juego1;

import java.util.Scanner;
import java.util.Random;

public class JuegoAdivinaNumero extends Juego {
    protected int numeroAAdivinar;
    private int vidasOriginales; 

    public JuegoAdivinaNumero(int numerodeVidas) { 
        super(numerodeVidas);
        this.vidasOriginales = numerodeVidas;
    }

    public boolean validaNumero(int n) {
        return (n >= 0 && n <= 10);
    }


    public void generaNumeroSecreto() {
        this.numeroAAdivinar = new Random().nextInt(11);
    }

    public void juega() {
        reiniciaPartida();
        generaNumeroSecreto();
        
        Scanner scanner = new Scanner(System.in);
        

        System.out.println("INICIANDO: " + this.getClass().getSimpleName());
        System.out.println("Vidas disponibles: " + numerodeVidas);
        
        while (numerodeVidas > 0) {
            System.out.print("Ingrese un numero: ");
            int intento = scanner.nextInt();

            if (validaNumero(intento)) {
                if (intento == numeroAAdivinar) {
                    System.out.println("GANASTE");
                    actualizaRecord();
                    break; 
                } else {
                    if (intento < numeroAAdivinar) {
                        System.out.println("es MAYOR.");
                    } else {
                        System.out.println("es MENOR.");
                    }
                    
                    if (!quitaVida()) {
                        System.out.println("PERDISTE. El numero era: " + numeroAAdivinar);
                    }
                }
            }
        }
    }

    @Override
    public void reiniciaPartida() {
        this.numerodeVidas = vidasOriginales;
    }
}