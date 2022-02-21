num = int(input("Digite um número"))
som = 1
print(f"Calculando {num}! = ", end='')
while num != 0:

    print(f"{num}  ", end='')
    print(f"x " if num > 1 else '= ', end='')
    som *= num
    num -= 1
print(som)
