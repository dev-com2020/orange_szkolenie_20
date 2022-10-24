import pickle

baza = open("baza1.data", "rb")
# baza = open(r"D:\orange\dzien3\test\baza1.data", "w")

odczyt = baza.read()
my_unpickled_obj = pickle.loads(odczyt)

print(my_unpickled_obj)

baza.close()

