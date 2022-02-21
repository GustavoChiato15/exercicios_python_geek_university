cont, lista, lista_impar = 1, [], []
while cont <= 10:
    n = -1
    while n < 0 or n > 50:
        n = int(input(f"\033[1;39m Digite o {cont}º número a ser adicionado a lista:"))
    lista.append(n)
    cont += 1
for element in lista:
    if element % 2 == 1:
        lista_impar.append(element)
print(f"""
A lista normal é essa:\033[4;31;40m{lista}\033[m
\033[1;39mA lista apenas com valores ímpares é essa \033[4;31;40m{lista_impar}\033[m
""")
