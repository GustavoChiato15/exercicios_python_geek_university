som = 0
cont = 0
for x in range(1, 11):
    n = int(input(f"Digite o {x}ºnúmero:"))
    som += n
    cont += 1
media = som/cont
print(f"A média entre os 10 números é {media}")