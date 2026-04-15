package Juego1;
import java.util.Random;

public class JuegoAdivinaPar extends JuegoAdivinaNumero {
    public JuegoAdivinaPar(int numerodeVidas) {
        super(numerodeVidas);
    }

    @Override
    public void generaNumeroSecreto() {
        Random r = new Random();
        this.numeroAAdivinar = r.nextInt(6) * 2;
    }

    @Override
    public boolean validaNumero(int n) {
        if (super.validaNumero(n) && n % 2 == 0) {
            return true;
        } else {
            System.out.println("ERROR solo numeros PARES entre 0 y 10.");
            return false;
        }
    }
}