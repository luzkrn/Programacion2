package Juego1;

public class Juego {
    protected int numerodeVidas;
    protected static int record;
    private int vidasIniciales;
    public Juego(int numerodeVidas) {
        this.numerodeVidas = numerodeVidas;
        this.vidasIniciales = numerodeVidas;
        this.record = 0;
    }

    
    public void reiniciaPartida() {
        this.numerodeVidas = this.vidasIniciales;
        System.out.println("Partida reiniciada. Vidas: " + numerodeVidas);
    }


    public void actualizaRecord() {
        record++;
        System.out.println(" record actualizado " + record);
    }

    public boolean quitaVida() {
        if (numerodeVidas > 0) {
            numerodeVidas--;
            System.out.println("Te queda(n) " + numerodeVidas + " vida(s).");
            return numerodeVidas > 0;
        }
        return false;
    }
}