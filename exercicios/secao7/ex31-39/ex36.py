lista_reais, cont = [], 1
while cont <= 10:
    num = float(input(f"Digite o {cont} número real a ser adicionado na lista: "))
    lista_reais.append(num)
    cont += 1
print(lista_reais)
lista_reais.sort()
print(lista_reais)
