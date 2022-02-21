cont, lista = 1, []
while cont <= 6:
    num = int(input(f"Digite o {cont}º número inteiro que será inserido na lista:\n"))
    lista.append(num)
    cont += 1
print(lista[::-1])
