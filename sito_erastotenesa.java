import java.util.Scanner;

public class Main {
    public static boolean[] sitoEratostenesaZoptymalizowane(int n) {
        boolean[] liczbyPierwsze = new boolean[n + 1];
        for (int i = 0; i <= n; i++) {
            liczbyPierwsze[i] = true;
        }
        liczbyPierwsze[0] = false;
        liczbyPierwsze[1] = false;

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (liczbyPierwsze[i]) {
                for (int j = i * i; j <= n; j += i) {
                    liczbyPierwsze[j] = false;
                }
            }
        }

        return liczbyPierwsze;
    }

    public static void main(String[] args) {
        // Wprowadzenie wartości n
        Scanner scanner = new Scanner(System.in);
        System.out.print("Podaj wartość n: ");
        int n = scanner.nextInt();

        // Wywołanie funkcji sitoEratostenesaZoptymalizowane i wypisanie wyniku
        System.out.println("Liczby pierwsze od 0 do " + n + ":");
        boolean[] tablica = sitoEratostenesaZoptymalizowane(n);

        for (int i = 2; i <= n; i++) {
            if (tablica[i]) {
                System.out.println(i);
            }
        }
    }
}
