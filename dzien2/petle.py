print("MENU:")
warunek = input("Wpisz 't' aby rozpocząć liczenie premii,")

while warunek == 't':
    sales = float(input("podaj wielkość sprzedaży: "))
    rate = float(input("podaj wysokość premii: "))

    wynik = sales * rate

    print("-" * 20)
    print("Premia wynosi:", format(wynik, '.2f'), ' zł', sep=' ✅ ')
    print("-" * 20)
    warunek = input("Czy chesz obliczyć kolejną premię?(t lub n): ")

print("To jest poza pętlą!!!")
