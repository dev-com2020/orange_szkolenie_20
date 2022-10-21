# print("MENU:")
# warunek = input("Wpisz 't' aby rozpocząć liczenie premii,")
#
# while warunek == 't':
#     sales = float(input("podaj wielkość sprzedaży: "))
#     rate = float(input("podaj wysokość premii: "))
#
#     wynik = sales * rate
#
#     print("-" * 20)
#     print("Premia wynosi:", format(wynik, '.2f'), ' zł', sep=' ✅ ')
#     print("-" * 20)
#     warunek = input("Czy chesz obliczyć kolejną premię?(t lub n): ")
#
# print("To jest poza pętlą!!!")


# licznik = 99
# while True:
#     licznik -= 1  # licznik = licznik + 1
#     print(licznik)
#     if licznik == 5:
#         break
#
#
# wybor = int(input("Ile razy mam wykonać ksero?"))
# for ksero in range(wybor):
#     print(ksero+1)
#     print("Robię ksero...")

import random

lista = []
ilosc = random.randint(3, 8)
for i in range(ilosc):
    lista.append(random.randint(1, 10))

# for i in lista:
#     print(f"elementy w liście:{i}")

krotka = ()

for i, w in enumerate(lista):
    print(f"indeks:{i}, element w liście:{w}")
    if w == 10:
        print("Znalazłem 10!!!")
        krotka += w,
        liczba1 = krotka[0]
        print("Dodajemy +5 do pierwszego indeksu krotki:", liczba1 + 5)

# slownik = {"imie": "Marek", "nazwisko": "Kowalski", "plec": "mezczyzna"}
#
# for k, w in slownik.items():
#     print(k)
#     print(w)
#
