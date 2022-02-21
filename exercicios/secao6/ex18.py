numlidos = int(input("Digite quantos números você quer que o programa rode:"))
maior = -99999999999999999999
som = 1
for x in range(0, numlidos):
    n = int(input("Digite um valor natural:"))
    if maior == n:
        som += 1
    if n > maior:
        maior = n
if maior > 0:
    print(f"O maior número é o {maior} e ele foi lido {som} vezes")