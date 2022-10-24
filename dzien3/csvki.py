import csv

# with open('test.csv', "r", encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile, delimiter=",")
#     for row in reader:
#         print(row[0])
#         print(row[1])
#         print(row[2])

# lista = []
# with open('test.csv', "r", encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#
#     for row in reader:
#         lista.append(row['kolumna 1'])
#         print(row['kolumna 2'])
#         print(row['kolumna 3'])
#
#     print(reader.fieldnames)
#     print(lista)

# lista1 = ['imie', 'nazwisko', 'pesel']
# lista2 = ['Jan', 'Kowalski', '14654665135']
#
# with open('test2.csv', "w", encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(lista1)
#     writer.writerow(lista2)

struc = {'imie': 'Jan',
         'nazwisko': 'Kowalski',
         'pesel': 145648423132
         }

struc2 = {'imie': 'Tomasz',
          'nazwisko': 'Kowalski',
          'pesel': 343438423132
          }

struc_l = [struc, struc2]

with open('test3.csv', "w", encoding='utf-8') as csvfile:
    fieldnames = ['imie', 'nazwisko', 'pesel']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in struc_l:
        writer.writerow(i)
