imie = "Tomek"  # string (łańcuch znaków)
print(type(imie))
wiek = 39
print(type(wiek))  # int (liczba całkowita)
temperatura = 36.6
print(type(temperatura))  # float (liczba zmiennoprzecinkowa)
czy_umiem_pythona = False  # bool (True/False)
print(type(czy_umiem_pythona))
coToZaTyp = 36, 6, 54, 34, 65, 45, "Janek", "Basia", 45
# print(type(coToZaTyp))
# print(len(coToZaTyp))
# print(coToZaTyp[-1])
# print(coToZaTyp[:3])
# print(coToZaTyp[-4:])
# print(coToZaTyp.count(45))
# print(coToZaTyp.index(45))

plec1 = "k", "m", 'mm', 'ttt'
(kobieta, *mezczyzna, nijaki) = plec1
# print(kobieta)
# print(mezczyzna)
# print(nijaki)

# print(plec1)
# plec2 = 1, 2
# print(plec2)
# final = plec1 + plec2
# print(final)

lista = list(mezczyzna)

lista.append(1983)
print(lista)
lista.pop(0)
lista.insert(0, "Tomek")
lista.remove(1983)
print(lista)

oceny = [6, 5, 4, 1, 2, 3]
oceny.sort()
print(oceny)
oceny.reverse()
print(oceny)
# oceny.clear()
oceny2 = ['dostateczny', 'mierny']
oceny3 = oceny2 + oceny
# oceny2.extend(oceny)
print(oceny3)

numery = [2, 3, 5]
cyfry = numery.copy()
numery = [2, 33, 5]
print(cyfry)
