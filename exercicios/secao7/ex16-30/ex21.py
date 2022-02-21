cont, lista_a, lista_b, lista_c = 1, [], [], []
while cont <= 10:
    num_a = int(input(f"Digite o {cont}º número para ser adicionado na lista a:"))
    lista_a.append(num_a)
    cont += 1
cont = 1
while cont <= 10:
    num_b = int(input(f"Digite o {cont}º número para ser adicionado na lista b:"))
    lista_b.append(num_b)
    cont += 1
for i in range(0, 10):
    lista_c.append(lista_a[i] - lista_b[i])
print(lista_a)
print(lista_b)
print(lista_c)
