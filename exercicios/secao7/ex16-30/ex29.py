cont_impar, soma_par, cont, lista, lista_par, lista_impar = 0, 0, 1, [], [], []
while cont <= 6:
    num = int(input(f"Digite o {cont}º número a ser inserido na lista:"))
    lista.append(num)
    cont += 1
for element in lista:
    if element % 2 == 0:
        lista_par.append(element)
        soma_par += element
    elif element % 2 == 1:
        lista_impar.append(element)
        cont_impar += 1
print(f"""
Desses números digitados: {lista}
Dos quais são pares: {lista_par}
Possuem soma: {soma_par}
Além disso os números ímpares são: {lista_impar}
E foram digitados um total de {cont_impar} números ímpares""")
