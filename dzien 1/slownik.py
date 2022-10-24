slownik = {1: "Tomek",
           "__wiek": 39,
           "hobby": ['programowanie', 'jedzenie']}

print(slownik.keys())
print(slownik['hobby'][0])
print(slownik.values())
print(slownik.items())
slownik["__wiek"] = 40
slownik["znakZ"] = "Ryby"
# slownik.pop('__wiek')
print(slownik.get("znakZ"))
# print(slownik)
# del slownik[1]
print(slownik)
print(len(slownik))
print(slownik.get("hobby")[0])
klucz, wartosc = slownik.popitem()
print(klucz)
print(wartosc)
