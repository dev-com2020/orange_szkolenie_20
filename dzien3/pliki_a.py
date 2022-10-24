# baza = open("baza3.data", "a")
baza = open("baza3.data", "r")

# slownik = {"jeden": "a", "dwa": "b"}
# lista = [34, 55, 66, 756, 9786]
#
# for i in lista:
#     baza.write(str(i) + '\n')

odczyt = baza.readline()
# print(odczyt)
# adresy = list(odczyt)
# print(adresy)
adresy = []

while odczyt != "":
    adres = int(odczyt)
    print(adres)
    odczyt = baza.readline()
    adresy.append(adres)

print(adresy)
baza.close()

for i in adresy:
    print(i)
