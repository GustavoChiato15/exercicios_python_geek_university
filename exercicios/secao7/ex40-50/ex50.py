matriz = []
soma = 0
for line in range(3):
    current_line = []
    for colun in range(3):
        num = int(input(f"Digite um valor para ser adicionado na linha {line} e coluna {colun} na matriz:"))
        current_line.append(num)
    matriz.append(current_line)
for i in range(3):
    for j in range(3):
        if j != 2:
            print(f"{matriz[i][j]}, ", end='')
        elif j == 2:
            print(f"{matriz[i][j]}", end='')
        if i == 1 and i == j:
            for valor_diagonal in range(1, i+1):
                soma += matriz[i][j] + matriz[i-valor_diagonal][1+valor_diagonal] +matriz[i+valor_diagonal][i-valor_diagonal]
                # pega o valor do meio + o valor superior direito + valor inferior esquerdo
    print('')
print(f"Soma = {soma}")