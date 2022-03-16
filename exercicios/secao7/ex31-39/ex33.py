cont, lista = 1, []
while cont <= 10:
    num = int(input(f"Digite o {cont}º número da lista:"))
    if num != 0:
        lista.append(num)
    cont += 1
print(lista)
