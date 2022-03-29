matriz = []
som, default_size = 0, 3
for line in range(default_size):
    current_line = []
    for colun in range(default_size):
        num = int(input(f"Digite o número a ser colocado na linha {line} e coluna {colun}"))
        current_line.append(num)
    matriz.append(current_line)
for line in range(default_size):
    for colun in range(default_size):
        print(f"{matriz[line][colun]} ", end='')
        if line != 0 and line == colun:
            for value_left in range(1, line+1):
                som += matriz[line][colun - value_left]
    print('')
print(f"Soma = {som}")
