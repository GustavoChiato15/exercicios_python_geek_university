cont_par, lista = 0, []

while cont_par <= 5:
    num = 3
    while num % 2 != 0:
        num = int(input(f"Digite o {cont_par+1}º número par:"))
    lista.append(num)
    cont_par += 1
print(lista[::-1])
