matriz = []
cont = 0
for line in range(1, 5):
    linha_atual = []
    for colun in range(1, 5):
        linha_atual.append(int(input(f"Digite o {colun} valor a ser adicionado na linha {line}")))
    for element in linha_atual:
        if element > 10:
            cont += 1
            print(f"elemento da lista {element} é maior que 10")
    matriz.append(linha_atual)
print(matriz)
print(f"A quantidade de elementos maiores que 10 na lista é: {cont}")