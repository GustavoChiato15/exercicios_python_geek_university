cont, lista_codigos, lista_alturas = 1, [], []
while cont <= 5:
    codigo = str(input(f"Digite o código do {cont}º aluno:"))
    lista_codigos.append(codigo)
    altura = float(input(f"Digite a altura do {cont}º aluno:"))
    lista_alturas.append(altura)
    cont += 1
codigo_maior = lista_alturas.index(max(lista_alturas))
codigo_menor = lista_alturas.index(min(lista_alturas))
print(f"O aluno que tem a maior altura que é de {max(lista_alturas):.2f}m"
      f" é o de código {lista_codigos[codigo_maior]}".replace('.', ','))
print(f"O aluno que tem a menor altura que é de {min(lista_alturas):.2f}m"
      f" é o de código {lista_codigos[codigo_menor]}".replace(".", ','))
