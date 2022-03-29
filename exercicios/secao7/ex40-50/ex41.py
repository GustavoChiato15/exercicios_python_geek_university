matriz = []
cont = 0
for line in range(0, 5):
    linha_atual = []
    for colun in range(0, 5):
        if colun == cont:
            linha_atual.append(1)
        else:
            linha_atual.append(0)
    cont += 1
    matriz.append(linha_atual)
for num in range(0, 5):
    print(matriz[num])
