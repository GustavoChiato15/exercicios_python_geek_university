soma = 0
lista = []
for _ in range(1, 9):
    element_int = int(input("Digite um número inteiro para ser adicionado na lista:"))
    lista.append(element_int)
x = int(input("Digite uma posição na lista para ser somada(0 á 7)"))
y = int(input("Digite outra posição na lista para ser somada(0 à 7)"))
print(f"A lista é essa: {lista}")
print(f"O elemento {lista[x]} na posição {x} ao ser somado com o elemento {lista[y]} na posição {y} retorna o resultado {lista[x]+ lista[y]}")
