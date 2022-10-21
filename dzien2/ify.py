# lista = []
# name = input("Jak masz na imię")
# age = int(input("Ile masz lat"))
#
# print(f"Witaj {name}")
# if age < 18:
#     print("Nie masz jeszcze 18 lat")
# elif age == 18:
#     print("Masz dokładnie 18 lat")
# elif age == 40:
#     print("40-latek")
# else:
#     print(f"masz {age} lat")
#     lista.append(age)
#
# lista.append(name)
# print(f"Poza instrukcją, Zawartość listy: {lista}")



# if temp < 20 and minuta > 10:
#     print("działa w and!")
#
# if temp < 20 or minuta > 10:
#     print("działa w or!")
#
# if not (temp > 100):
#     print("działa w not")

temp = int(input("Podaj temperaturę "))
if temp < 20:
    minuta = int(input("Podaj minutę "))
    if minuta > 10:
        print("Parametry są właściwe")


