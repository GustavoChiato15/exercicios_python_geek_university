cont = 1
lista_x, lista_y, lista_soma, lista_produto, lista_diferenca, lista_intersecao, lista_uniao = [], [], [], [], [], [], []
while cont <= 5:
    num = int(input(f"Digite o {cont}º número do vetor x:"))
    while num in lista_x:
        num = int(input(f"Digite outro {cont}º valor que ainda não está nos vetores:"))
    lista_x.append(num)
    cont += 1
cont = 1
while cont <= 5:
    num = int(input(f"Digite o {cont}º número do vetor y:"))
    while num in lista_y:
        num = int(input(f"Digite outro {cont}º valor que ainda não está nos vetores"))
    lista_y.append(num)
    cont += 1
for element in range(0, 5):
    lista_soma.append(lista_x[element] + lista_y[element])
    lista_produto.append(lista_x[element] * lista_y[element])
    lista_uniao.append(lista_x[element])
    if lista_x[element] not in lista_y:
        lista_diferenca.append(lista_x[element])
    if lista_x[element] in lista_y:
        lista_intersecao.append(lista_x[element])
    if lista_y[element] not in lista_x:
        lista_uniao.append(lista_y[element])
lista_uniao.sort()
print(f"""
A lista x é {lista_x}
A lista y é {lista_y}
A soma entre os elementos das listas é {lista_soma}
O produto entre os elementos das listas é {lista_produto}
Os elementos da lista x que não estão na lista y é {lista_diferenca}
Os elementos que aparecem nas 2 listas são {lista_intersecao}
A união entre as listas é {lista_uniao}
""")
