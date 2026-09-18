from math import (asin, log, e, pow)

a, b, x = map(float, input("введите значения a, b, x через пробел\n").split())
y = 0

if 3 * a - b > 0:
    y = 2 * log(x) - pow(e, (a * x - b) / 10)
elif 3 * a - b <= 0:
    y = asin(x / 10)

print("Вычисленное значение y:", y)
