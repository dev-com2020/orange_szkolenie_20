
# name = input("Jak masz na imię")
# age = int(input("Ile masz lat"))

# print(f"Witaj {name}")
# if age < 18:
#     print("Nie masz jeszcze 18 lat")
# elif age == 18:
#     print("Masz dokładnie 18 lat")
# elif age > 18:
#     print("Masz więcej niż 18 lat")


temp = int(input("Podaj temperaturę "))
minuta = int(input("Podaj minutę "))

if temp < 20 and minuta > 10:
    print("działa w and!")

if temp < 20 or minuta > 10:
    print("działa w or!")

if not (temp > 100):
    print("działa w not")