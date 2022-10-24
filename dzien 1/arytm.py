import datetime
from datetime import datetime as dt
import time
import pytz

suma = 1 + 2 * 3 / 4 ** 2
print("Wynik operacji:", suma, "(po zaokrągleniu)")
print("Wynik operacji: %.1f (po zaokrągleniu)" % suma)
print("Wynik operacji: {:.1f} (po zaokrągleniu)".format(suma))
print(f"Wynik operacji: {suma} (po zaokrągleniu)")
print("Wynik operacji: " + str(suma) + " (po zaokrągleniu)")

liczba = 1234567890
print("Nasza duża liczba to: {:,}".format(liczba))

rok = 2022
miesiac = 10
dzien = 21

data = datetime.datetime(rok, miesiac, dzien, 10, 00, 00)
print(data)
seconds = time.time()
local = time.ctime(seconds)
print("Sekundy:", seconds)
# time.sleep(5)
print("Czas lokalny:", local)

time_str = time.strftime("%d %m %Y\n%H:%M:%S")
print(time_str)


tz_NY = pytz.timezone('America/New_York')
datetime_NY = dt.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = dt.now(tz_London)
print("London time:", datetime_London.strftime("%H:%M:%S"))

tz_Warsaw = pytz.timezone('Europe/Warsaw')
datetime_Waw = dt.now(tz_Warsaw)
print("Warsaw time:", datetime_Waw.strftime("%H:%M:%S"))
