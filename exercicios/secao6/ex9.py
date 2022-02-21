num = int(input("Digite um número inteiro:"))
for n in range(num):
    if n % 2 == 1:
        print(f"{n} é um número ímpar menor que {num}")