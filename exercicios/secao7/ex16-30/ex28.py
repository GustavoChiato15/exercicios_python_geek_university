cont, lista, lista_1, lista_2 = 1, [], [], []
while cont <= 10:
    num = int(input(f"Digite o {cont}º número da lista:"))
    lista.append(num)
    cont += 1
for element in lista:
    if element % 2 == 1:
        lista_1.append(element)
    elif element % 2 == 0:
        lista_2.append(element)
print(f"A lista 1 {lista_1} possui {len(lista_1)} elementos")
print(f"A lista 2 {lista_2} possui {len(lista_2)} elementos")
