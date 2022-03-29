matriz = []
for line in range(10):
    linha_atual = []
    for colun in range(10):
        if line < colun:
            linha_atual.append(2*line+7*colun-2)
        elif line == colun:
            linha_atual.append((3*line)**2-1)
        elif line > colun:
            linha_atual.append((4*line)**3-(5*colun)**2 + 1)
    for element in range(10):
        if element != 9:
            print(f"{linha_atual[element]:<4}, ", end='')
        else:
            print(f"{linha_atual[element]:<4}")

    matriz += linha_atual
