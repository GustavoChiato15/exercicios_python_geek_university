matriz_1, matriz_2, matriz_maior = [], [], []
for line in range(4):
    linha_atual = []
    for colun in range(4):
        num = int(input(f"Digite o valor da linha {line+1} e coluna {colun+1} para ser inserido na matriz 1:"))
        linha_atual.append(num)
    matriz_1 += linha_atual
for line in range(4):
    linha_atual = []
    for colun in range(4):
        num = int(input(f"Digite o valor da linha {line+1} e da coluna {colun+1} para ser inserido na matriz 2:"))
        linha_atual.append(num)
    matriz_2 += linha_atual
print("MATRIZ 1:", end='')
for element in range(0, 16):
    print(f"{matriz_1[element]:<8},", end='')
print('')
print("MATRIZ 2:", end='')
for element in range(0, 16):
    print(f"{matriz_2[element]:<6},", end='')
print('')
for element in range(0, 16):
    if matriz_1[element] > matriz_2[element]:
        matriz_maior.append(matriz_1[element])
    elif matriz_2[element] > matriz_1[element]:
        matriz_maior.append(matriz_2[element])
print(f"Número maior das matrizes:{matriz_maior}")
