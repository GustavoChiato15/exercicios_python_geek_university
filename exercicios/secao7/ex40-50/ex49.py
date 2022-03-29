matriz = []
soma = 0
for line in range(3):
    current_line = []
    for colun in range(3):
        num = int(input(f"Digite um valor para ser adicionado na linha {line} e coluna {colun} da matriz:"))
        current_line.append(num)
    matriz.append(current_line)
for i in range(3):
    for j in range(3):
        if j != 2:
            print(f'{matriz[i][j]}, ', end='')
        elif j == 2:
            print(f'{matriz[i][j]}', end='')
        if i == j:
            soma += matriz[i][j]
    print('')
print(f"A soma dos elementos localizados na diagonal da matriz é: {soma}")
