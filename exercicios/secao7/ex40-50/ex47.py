matriz = []
soma, cont, size = 0, 0, 3
for line in range(size):
    lis_curr_line = []
    for colun in range(size):
        num_lis = int(input(f"Digite um número para ser adicionado na linha {line} coluna {colun}: "))
        lis_curr_line.append(num_lis)
    matriz.append(lis_curr_line)
for line in range(size):
    for colun in range(size):
        print(f"{matriz[line][colun]} ", end='')
        if line != 0 and line == colun:
            for num_acima in range(1, line+1):
                soma += matriz[line - num_acima][colun]
    print('')
print(f"A soma dos números acima da diagonal é {soma}")
