warunek = 't'

while warunek == 't':
    sales = float(input("podaj wielkość sprzedaży: "))
    rate = float(input("podaj wysokość premii: "))

    wynik = sales * rate

    print("Premia wynosi:", format(wynik, '.2f'), 'zł', sep='')


