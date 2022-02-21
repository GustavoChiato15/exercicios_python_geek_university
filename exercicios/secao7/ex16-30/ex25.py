cont, lista_total, lista_t_7, lista_n_mult, lista_e_mult = 1, [], [], [], [7, 77]
while len(lista_total) <= 100:
    resultado = cont * 7
    lista_resultado = list(str(resultado))
    if lista_resultado[-1] == '7':
        if resultado <= 100:
            lista_total.append(resultado)
    else:
        lista_e_mult.append(resultado)
    if cont not in lista_e_mult:
        lista_total.append(cont)
    lista_total.sort()
    cont += 1
print(lista_total)
