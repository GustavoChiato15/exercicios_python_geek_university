lista = []
cont = 1
for _ in range(1, 11):
    num = int(input(f"Digite o {cont}º número inteiro para ser adicionado na lista(max numeros 10):"))
    lista.append(num)
    cont += 1
print(lista)
for posicao, element in enumerate(lista):
    if element % 2 == 0:
        print(f" O número par {element} esta na posicao {posicao}")
