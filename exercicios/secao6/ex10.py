soma = 0
for x in range(1, 101):
    if x % 2 == 0:
        soma += x
        print(x)
print(f"A soma é {soma}")