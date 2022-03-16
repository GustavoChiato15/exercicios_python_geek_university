cont, lista_a, lista_b, lista_uniao = 1, [], [], []
while cont <= 10:
    num = int(input(f"Digite o {cont}º número da lista a:"))
    lista_a.append(num)
    cont += 1
cont = 1
while cont <= 10:
    num = int(input(f"Digite o {cont}º número da lista b:"))
    lista_b.append(num)
    cont += 1
for element in lista_a:
    if element not in lista_uniao:
        lista_uniao.append(element)
for element in lista_b:
    if element not in lista_uniao:
        lista_uniao.append(element)
print(lista_a)
print(lista_b)
print(lista_uniao)
