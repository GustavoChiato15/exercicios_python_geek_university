cont, lista = 1, []
while cont <= 10:
    num = int(input(f"Digite o {cont}º número da lista:"))
    lista.append(num)
    cont += 1
x = int(input("Digite um número inteiro"))
for element in lista:
    for n in range(1, element+1):
        if x * n == element:
            print(f"O número {element} é múltiplo de {x} porque {n} x {x} é {element}")
