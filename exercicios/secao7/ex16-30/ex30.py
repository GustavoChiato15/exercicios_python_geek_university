cont, lista_a, lista_b, lista_intersecao = 1, [], [], []
while cont <= 10:
    num = int(input(f"Digite o {cont}º número para ser inserido na lista a:"))
    lista_a.append(num)
    cont += 1
cont = 1
while cont <= 10:
    num = int(input(f"Digite o {cont}º número para ser inserido na lista b"))
    lista_b.append(num)
    cont += 1
for element in lista_a:
    if element not in lista_intersecao:
        lista_intersecao.append(element)
for element in lista_b:
    if element not in lista_intersecao:
        lista_intersecao.append(element)
lista_a.sort()
lista_b.sort()
lista_intersecao.sort()
print(lista_a)
print(lista_b)
print(lista_intersecao)
