def calc_fatorial(numero):
    total = 1
    if numero >= 2:
        for n in range(1, numero+1):
            total *= n
    return total


n_colun = []
n_linhas = int(input("Digite o número de linhas que deseja que o programa tenha: "))
for linha in range(0, n_linhas):
    #print(f"A linha é {linha}")
    for colun in range(0, linha+1):
        #print(f"A coluna é {colun}")
        if linha == colun or colun == 0:
            n_colun.append(1)
        else:
            n_colun.append(int(calc_fatorial(linha)/(calc_fatorial(colun)*calc_fatorial(linha - colun))))
    print(n_colun)
    n_colun.clear()
