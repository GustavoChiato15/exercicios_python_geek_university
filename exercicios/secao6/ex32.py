from math import gcd
def mmc(numeros):
    m = 1
    for n in numeros:
        m = m * n
    return m
numeros = range(1, 10)
print(mmc(numeros))
