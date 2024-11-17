# Sito Eratostenesa

## 1. Co to jest?
**Polega na wyznaczaniu liczby pierwszych z przedziału ⟨2, n⟩ n∈ℕ.**

Jest to znacznie lepszy sposób niż sprawdzanie pierwszości liczby
dla każdej kolejnej wartości z przedziału.

### Zalety:
- **Złożoność obliczeniowa** to `O(n*log log(n))`. To oznacza, że algorytm jest relatywnie szybki.

### Wady:
- **Złożoność pamięciowa** to `O(n)` - złożoność liniowa. Algorytm zajmuje dużo pamięci i przy większych liczbach będzie to problematyczne. W takim przypadku warto posłużyć się innymi algorytmami. 

## 2. Działanie Sita

1. Stwórz listę dla indeksów z przedziału ⟨0, n⟩. Wszystkie wartości mają być `true`.
2. Ustaw `pierwsze[0] = false` i `pierwsze[1] = false`.
3. Wybierz najmniejszą liczbę z przedziału ⟨2, n⟩. Jest to `2`, która jest liczbą pierwszą.
4. Dla większych wielokrotności liczby `2` ustaw wartość `false`. Przykład: `pierwsze[4] = false`
5. Wybierz kolejną liczbę `x` z przedziału ⟨2, n⟩. Jeśli `pierwsze[x] = true`, to znaczy, że `x` jest liczbą pierwszą. Wtedy ustaw wartość `false` dla większych wielokrotności `x`.
6. Powtarzaj krok 5 dla `x∈⟨2, √n⟩`

**Pamiętaj!**
- Usuwając wielokrotności liczby pierwszej, zacznij od jej kwadratu! Nie ma sensu usuwać mniejszych wielokrotności, gdyż zostały już usunięte. Pomoże to w optymalizacji algorytmu.

## 3. Implementacja Sita w programowaniu

## 4. Zadania

### Znajdź liczby pierwsze z przedziału:
- ⟨2, 60⟩
- ⟨2, 80⟩
- ⟨2, 100⟩

### Rozłóż na czynniki pierwsze:
- 42
- 64
- 97

## 5. Źródła

### Kanał „Matura Informatyka – Małgorzata Piekarska”
https://www.youtube.com/watch?v=xo2aoAMN-4A
### korepetycjezinformatyki.pl
https://www.korepetycjezinformatyki.pl/sito-eratostenesa/
### algorytm.edu.pl
https://www.algorytm.edu.pl/algorytmy-maturalne/sito-eratostenesa.html
https://www.algorytm.edu.pl/matura-informatyka/zlozonosc-algorytmu
### eduinf.waw.pl
https://eduinf.waw.pl/inf/alg/001_search/0011.php
