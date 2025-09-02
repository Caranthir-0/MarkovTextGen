# Markov Sentence Generator

Prosty generator pseudo-zdań oparty na łańcuchach Markowa (trigramy).

Projekt napisany w Pythonie – idealny do eksperymentów z przetwarzaniem języka naturalnego.

---

## 📌 Jak działa?

1. Wczytuje plik tekstowy (`.txt`) jako korpus.

2. Dzieli tekst na tokeny (słowa).

3. Buduje trigramy: każda para słów (head) wskazuje na możliwe kolejne słowo (tail).

4. Tworzy model Markowa (mapa przejść).

5. Generuje losowe zdania na podstawie prawdopodobieństw przejść.

---

## ✅ Wymagania

- Python 3.8+

- Brak dodatkowych bibliotek (używa tylko standardowej biblioteki Pythona).

---

## ▶️ Jak uruchomić?

1. Umieść swój plik tekstowy w tym samym katalogu co skrypt.

2. Uruchom w terminalu:

python main.py

3.  Podaj nazwę pliku (bez rozszerzenia lub z  `.txt`), np.:

```
corpus

```

4.  Skrypt wygeneruje  **10 pseudo-zdań**  na podstawie Twojego korpusu.

----------

## ⚙️ Parametry w kodzie

-   `min_len=5`  – minimalna długość zdania (możesz zmienić w funkcji  `generate_pseudo_sentence`).
-   Domyślnie generuje 10 zdań (zmień w pętli w  `main()`)
  

----------

## 🔍 Przykład działania

Dla korpusu:

```
Ala ma kota. Ala ma psa. Kot śpi. Pies biega.

```

Przykładowe wyjście:

```
Ala ma kota. Ala ma psa.
Kot śpi. Pies biega.
Ala ma kota. Kot śpi.

```
