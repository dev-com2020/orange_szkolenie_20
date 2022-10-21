# dni_tyg = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
# print(len(dni_tyg))
# print(dni_tyg[2:6])

dni_tyg = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
dni_pobrane = []
for i, w in enumerate(dni_tyg):
    if i > 1 and i < 6:
        dni_pobrane.append(w)
print(dni_pobrane)



