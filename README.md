# Sito Eratostenesa

## 1. Co to jest?
**Polega na wyznaczaniu liczby pierwszych z przedziału ⟨2, n⟩ n∈ℕ.**

Jest to znacznie lepszy sposób niż sprawdzanie pierwszości liczby
dla każdej kolejnej wartości z przedziału.

Zalety:
- **Złożoność obliczeniowa** to `O(n*log log(n))`. To oznacza, że algorytm jest relatywnie szybki.

Wady:
- **Złożoność pamięciowa** to `O(n)` - złożoność liniowa. Algorytm zajmuje dużo pamięci i przy większych liczbach będzie to problematyczne. W takim przypadku warto posłużyć się innymi algorytmami. 

## 2. Działanie Sita

1. Stwórz listę dla indeksów z przedziału ⟨2, n⟩. Wszystkie wartości mają być `true`.
2. Ustaw przedział dla liczb ⟨2, n⟩
3. Zacznij odsiewać liczby pierwsze, które należą do ⟨2, √n⟩

**Pamiętaj!**
- Usuwając wielokrotności liczby pierwszej, zacznij od jej kwadratu! Nie ma sensu usuwać mniejszych wielokrotności, gdyż zostały już usunięte. Pomoże to w optymalizacji algorytmu.

## 3. Implementacja Sita w programowaniu

## 4. Zadania

Znajdź liczby pierwsze z przedziału:
- ⟨2, 60⟩
- ⟨2, 80⟩
- ⟨2, 100⟩

Rozłóż na czynniki pierwsze:
- 42
- 64
- 97

- 
