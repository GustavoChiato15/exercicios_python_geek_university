n = int(input(f'Digite o número de linhas: '))
cont = 1
for linhas in range(1, n + 1):
    for colunas in range(1, linhas + 1):
        print(f"{cont:<3}", end='')
        cont += 1
    print()
