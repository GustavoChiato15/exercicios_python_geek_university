som = 0
somi = 1
n1 = int(input("Digite um número inteiro:"))
n2 = int(input("Digite outro número inteiro:"))
if n1 < n2:
    for n in range(n1, n2+1):
        if n % 2 == 0:
            som += n
        if n % 2 == 1:
            somi *= n
elif n2 < n1:
    for n in range(n2, n1+1):
        if n % 2 == 0:
            som += n
        if n % 2 == 1:
            somi *= n
print(f"A soma dos números pares entre os números citados é {som} e a multiplicação dos números ímpares é {somi}")
