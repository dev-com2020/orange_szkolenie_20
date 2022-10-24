baza = open("baza2.data", "r", encoding="utf-8")
# baza = open(r"D:\orange\dzien3\test\baza1.data", "w")

odczyt = baza.readline()
odczyt2 = baza.readline()
odczyt3 = baza.readline()
odczyt4 = baza.readline()

odczyt = odczyt.rstrip('\n')
odczyt2 = odczyt2.rstrip('\n')
odczyt3 = odczyt3.rstrip('\n')

print(odczyt)
print(odczyt2)
print(odczyt3)
print(odczyt4)

baza.close()