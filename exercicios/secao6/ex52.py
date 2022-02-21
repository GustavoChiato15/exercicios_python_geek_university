qtprimo = -1
cont, soma, num = 0, 0, 2
while qtprimo <= 0:
    qtprimo = int(input("Digite um número inteiro positivo:"))
while cont < qtprimo:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print("primo", num)
        soma += num
        cont += 1
    num += 1
print(f' .A soma dos números é {soma}')



