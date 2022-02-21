lista_int = []
cont = 1
for x in range(1, 7):
    num = int(input(f"Digite o {cont}º número para ser mostrado no final do programa:"))
    lista_int.append(num)
    cont += 1
for element in lista_int:
    print(f'{element}. ', end='')