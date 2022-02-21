cont, lista_a, lista_b, lista_c = 1, [], [], []
while cont <= 10:
    num = int(input(f"Digite o {cont} número da lista A:"))
    lista_a.append(num)
    cont += 1
cont = 1
while cont <= 10:
    num = int(input(f"Digite o {cont} número da lista B:"))
    lista_b.append(num)
    cont += 1
for element in range(0, 10):
    if element % 2 == 0:
        lista_c.append(lista_a[element])
    elif element % 2 == 1:
        lista_c.append(lista_b[element])
print(lista_a)
print(lista_b)
print(lista_c)