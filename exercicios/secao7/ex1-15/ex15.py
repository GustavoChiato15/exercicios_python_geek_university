cont, lista, lista_repetidos = 1, [], []
while cont <= 20:
    num = int(input(f"Digite o {cont} número para ser inserido na lista:"))
    lista.append(num)
    if num in lista and num not in lista_repetidos:
        lista_repetidos.append(num)
    cont += 1
print(f"A lista normal é essa:{lista}")
print(f"A lista sem repetição é essa: {lista_repetidos}")
