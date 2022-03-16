lista, cont = [], 1
while cont <= 10:
    num = int(input(f"Digite o {cont}º valor para ser adicionado na lista"))
    lista.append(num)
    lista.sort()
    cont += 1
print(lista)
