cont, lista, lista_duplicados = 1, [], []
while cont <= 10:
    num = int(input(f"Digite o {cont}º número para ser adicionado na lista"))
    lista.append(num)
    cont += 1
lista_bkp = lista.copy()
for element in lista[::]:
    lista_bkp.pop(0)
    if element in lista_bkp:
        lista_duplicados.append(element)
        print(element)
print(f"Os valores digitados mais de uma vez pelo usuário foram: {lista_duplicados}")
