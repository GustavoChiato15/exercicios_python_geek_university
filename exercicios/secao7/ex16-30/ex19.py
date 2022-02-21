num, cont, lista = 0, 1, []
while cont <= 50:
    lista.append((num + 5 * num) % (num+1))
    cont += 1
    num += 1
print(lista)