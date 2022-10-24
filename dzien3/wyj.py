from decimal import Decimal, ROUND_UP


print(Decimal(0.5).quantize(Decimal(), rounding=ROUND_UP))

print(round(0.5))
