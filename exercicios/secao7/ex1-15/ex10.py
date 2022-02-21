soma, peso, cont, lista_notas = 0, 0, 1, []
while cont <= 15:
    nota = -1
    while 0 > nota or nota > 10:
        nota = float(input(f"Digite a nota do {cont}º aluno(0 a 10):"))
    lista_notas.append(nota)
    cont += 1
lista_notas.sort()
print(lista_notas)
for element in lista_notas:
    soma += element
    peso += 1
print(f"A média das notas dos 15 alunos é {soma/peso:.2f}".replace(".", ","))
