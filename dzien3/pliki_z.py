import pickle

baza = open("baza1.data", "wb")
# baza = open(r"D:\orange\dzien3\test\baza1.data", "w")

slownik = {"jeden": "a", "dwa": "b"}

my_pickled_obj2 = pickle.dumps(slownik)

baza.write(my_pickled_obj2)

baza.close()