som = 0
cont = 0
n= 1
for x in range(1, 11):
    n = int(input("Digite um número inteiro positivo"))
    while n < 0:
        n = int(input("Por favor digite novamente o número positivo:"))
    som += n
    cont += 1
media = som/cont
print(f"A média entre os {cont} números é {media}")