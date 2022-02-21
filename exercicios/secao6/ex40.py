somidade= 0
cont = 0
while True:
    print("Digite 0 para encerrar o programa")
    idade = int(input("Digite a idade de um indíviduo do grupo:"))
    if idade == 0:
        break
    cont += 1
    somidade += idade
print(f"A media da idade dos indivíduos é {somidade/cont}" if somidade > 0 else "Programa encerrado :( Fui morto")