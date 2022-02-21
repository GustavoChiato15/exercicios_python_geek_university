from termcolor import colored
cont, lista = 1, []
print("\033[1;30;48m Será atribuído 0 a valores negativos")
while cont <= 10:
    num = int(input(f"\033[mDigite o {cont}º número inteiro:"))
    if num < 0:
        num = 0
    lista.append(num)
    cont += 1
print(f"A lista ficou assim: {lista}")
