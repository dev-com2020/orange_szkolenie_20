def dodaj():
    a = 2
    b = 5
    print("Suma=", a + b)

def odejmij():
    pass

def pomnoz():
    pass

def podziel():
    pass

while True:
    print('''
       *** MENU ***
        1. dodaj
        2. odejmij
        3. pomnóż
        4. podziel 
        5. koniec
        ''')
    w = input("Mój wybór: ")
    if w == "1":
        dodaj()
    elif w == "2":
        odejmij()
    elif w == "3":
        pomnoz()
    elif w == "4":
        podziel()
    elif w == "5":
        break
    else:
        print("Nie ma takiej opcji, spróbuj ponownie")
