booleano = False
while booleano != True:
    n = int(input("Digite um número inteiro"))
    if n == 1000:
        booleano = True
    if n % 2 == 0:
        print("número par")
    else:
        print("número ímpar")

