cont, lista, lista_primos = 1, [], []
while cont <= 10:
    num = int(input(f"Digite o {cont}º número da lista:"))
    lista.append(num)
    cont += 1
for element in lista:
    contagem_divisiveis = 0
    for n in range(1, element+1):
        if element % n == 0:
            contagem_divisiveis += 1
    if contagem_divisiveis <= 2 and element != 1:
        lista_primos.append(element)
print(lista)
for pos, valor in enumerate(lista):
    if valor in lista_primos:
        print(f"A posição do valor {valor} na lista é a {pos}ª")
