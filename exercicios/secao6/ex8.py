menorvalor = 0
maiorvalor = 0
for x in range(1, 11):
    n = int(input(f"Digite o {x}º número de 10:"))
    if x == 1:
        menorvalor = n
        maiorvalor = n
    else:
        if n > maiorvalor:
            maiorvalor = n
        if n < menorvalor:
            menorvalor = n
print(f"O menor valor é {menorvalor} e o maior valor é {maiorvalor}")