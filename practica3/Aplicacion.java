package Juego1;

public class Aplicacion {
    public static void main(String[] args) {

        JuegoAdivinaNumero juegoGeneral = new JuegoAdivinaNumero(5);
        JuegoAdivinaPar juegoPar = new JuegoAdivinaPar(5);
        JuegoAdivinaImpar juegoImpar = new JuegoAdivinaImpar(5);

        System.out.println("PRIMER JUEGO ADIVNA EL NUMERO");
        juegoGeneral.juega();

        System.out.println("\nPresione Enter para el siguiente juego...");
        

        System.out.println("SEGUNDO JUEGO ADIVINA EL NUMERO PAR");
        juegoPar.juega();

        System.out.println("\nPresione Enter para el último juego...");


        System.out.println("TERCER JUEGO ADIVINA EL JUEGO IMPAR");
        juegoImpar.juega();

    }
}