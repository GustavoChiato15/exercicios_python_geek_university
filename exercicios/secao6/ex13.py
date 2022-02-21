num = int(input("Digite um número inteiro positivo par:"))
while num % 2 == 1:
    num = int(input("O valor não é par"))
for x in range(0, num+1):
    if x % 2 == 0:
        print(x)
