som, cont_neg, cont, lista, lista_neg, lista_pos = 0, 0, 1, [], [], []
while cont <= 10:
    num = float(input(f"Digite o {cont}º número real para ser inserido na lista:"))
    lista.append(num)
    cont += 1
for element in lista:
    if element < 0:
        cont_neg += 1
        lista_neg.append(element)
    elif element > 0:
        som += element
        lista_pos.append(element)
print(f"A quantidade de números negativos é {cont_neg}. São eles: {lista_neg}")
print(f"A soma dos números positivos é {som}. São eles: {lista_pos}")