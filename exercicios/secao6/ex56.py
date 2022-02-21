from time import sleep
soma, cont = 0, 0
maior, menor, cont_par, soma_par = 0, 0, 0, 0

while True:
    if cont == 0:
        n = int(input("Digite um número\n"))
        if n % 2 == 0:
            cont_par += 1
            soma_par += n
        maior, menor = n, n
        soma += n
    else:
        n = int(input("Digite outro número, digite 0 para parar\n"))
        sleep(1)
        if n == 0:
            break
        else:
            soma += n
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
            if n % 2 == 0:
                cont_par += 1
                soma_par += n
    cont += 1
print(f"\nA soma dos números digitados é {soma}")
print(f"A quantidade dos números digitados é {cont}")
print(f"A média dos números digitados é {soma/cont}")
print(f"O maior número digitado foi o {maior}, e o menor foi o {menor}")
print(f"A média dos números pares é {soma_par/cont_par}")