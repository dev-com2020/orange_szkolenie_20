import pickle
import dill

number = 35
tekst = "Witam"
lista = [1, 4, 6]
slownik = {"jeden": "a", "dwa": "b"}
krotka = (22, 33)

my_pickled_obj = pickle.dumps(tekst)
my_pickled_obj1 = pickle.dumps(lista)
my_pickled_obj2 = pickle.dumps(slownik)

print(f"Moja tekstowa zmienna:{my_pickled_obj}")
print(f"Moja listowa zmienna:{my_pickled_obj1}")
print(f"Moja slownikowa zmienna:{my_pickled_obj2}")

kwadrat = lambda x: x * x
moj_pickel = dill.dumps(kwadrat)
print(moj_pickel)

my_unpickled_obj = pickle.loads(my_pickled_obj1)
print(my_unpickled_obj)