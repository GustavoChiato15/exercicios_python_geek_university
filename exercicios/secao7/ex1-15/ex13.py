cont, lista = 1, []
while cont <= 5:
    num = int(input(f"Digite o {cont} número à ser adicionado na lista:\n"))
    lista.append(num)
    cont += 1
maior = max(lista)
menor = min(lista)
print(lista)
print(f"O maior valor é {maior} e se encontra na {lista.index(maior)+1}ª posição")
print(f"O menor valor é {menor} e se encontra na {lista.index(menor)+1}ª posição")
