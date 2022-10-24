from dzien3 import klasa1 as k1

adam = k1.Czlowiek()
adam.imie = "Adam"
adam.plec = "m"
adam.wiek = 20

adam.powitanie()
adam.spacer()

ewa = k1.Czlowiek()
ewa.imie = "Ewa"
ewa.plec = "k"
ewa.wiek = 19
print(ewa.wiek)

ewa.powitanie()
ewa.spacer()

# cosik = k1.Czlowiek()
# cosik.powitanie()
# cosik.spacer()
# print(cosik.__wiek)

# adam2 = k1.Czlowiek2("Adam2", 18, "m")
# adam2.powitanie()
# adam2.spacer()
# print(adam2.__wiek)
#
# lista_klas = [ewa, adam2, adam]
# print(lista_klas)

slownik = {"imie": "Tomek", "wiek": 10}

# adam2 = k1.Czlowiek2("Adam2", 20, "m")
# adam2.powitanie()
# adam2.spacer()
# print(adam2.__wiek)

robot = k1.Android("robot1")
robot.powitanie()
robot.spacer()
robot.lasery()
robot.numSeryjny()



# adam3 = k1.Czlowiek2(lista, 20)
# adam3.powitanie()


# To jest mój pierwszy program
#
# print("Python")
# print('Python')
# # print('👽👽👽')
#
# print('''
#     *************
#     *  👽👽👽  *
#     *************
#     ''')
# input("Aby zakończyć wciśnij ENTER!")  # to jest instrukcja, która wprowadza dane z klawiatury
