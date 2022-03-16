cont, lista = 1, []
while cont <= 10:
    num = int(input(f"Digite o {cont}º número a ser adicionado na lista:"))
    while num in lista:
        num = int(input(f"Digite o {cont}º número que seja diferente dos outros valores anteriores a ele na lista:"))
    lista.append(num)
    cont += 1
print(lista)