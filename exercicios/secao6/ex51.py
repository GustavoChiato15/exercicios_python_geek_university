num = int(input("Digite um número inteiro maior que um:"))
primo = False
cont = 0
for n in range(num, 0, -1):
    if num % n == 0:
        cont += 1
if cont == 2:
    print("O número é primo")