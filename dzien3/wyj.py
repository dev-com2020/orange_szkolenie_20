from decimal import Decimal, ROUND_UP


# print(Decimal(0.5).quantize(Decimal(), rounding=ROUND_UP))
# print(round(0.5))


def mnozenie(a, b):
    try:
        print("Wynik działania:", a * b)
    except TypeError:
        print("Błędne dane lub ich brak")
    else:
        print("Udało się prawidłowo pomnożyć")
    finally:
        lista = []
        lista.append(a)
        lista.append(b)
        print("Elementy:", lista)


invalid_age = [{'name': 'Jan', 'age': 'age'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]

def check_age(users, age):
    count = 0
    for user in users:
        try:
            if int(user['age']) < age:
                count += 1
        except (TypeError, KeyError, ValueError, ImportError):
            print("Niepoprawne dane: {}".format(user))
    return count


def check_age2(users, age):
    count = 0
    for user in users:
        try:
            if int(user['age']) < age:
                count += 1
        except TypeError:
            print("Niepoprawne dane: {}".format(user))
        except KeyError:
            print("Niepoprawne klucze: {}".format(user))
        except ValueError:
            print("Niepoprawne wiek: {}".format(user))
    return count


def check_age3(users, age):
    count = 0
    for user in users:
        try:
            if int(user['age']) < age:
                count += 1
        except Exception as e:
            print("Wystąpił błąd:", e)
    return count





# mnozenie(5, 5)
# print(mnozenie(5, 0))
# mnozenie("5", "5")

# print(mnozenie("5"))
