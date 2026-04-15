package Juego1;
import java.util.Random;

public class JuegoAdivinaImpar extends JuegoAdivinaNumero {
    public JuegoAdivinaImpar(int numerodeVidas) {
        super(numerodeVidas);
    }

    @Override
    public void generaNumeroSecreto() {
        Random r = new Random();
        this.numeroAAdivinar = r.nextInt(5) * 2 + 1;
    }

    @Override
    public boolean validaNumero(int n) {
        if (super.validaNumero(n) && n % 2 != 0) {
            return true;
        } else {
            System.out.println("ERRO solo numeros IMPARES entre 0 y 10.");
            return false;
        }
    }
}