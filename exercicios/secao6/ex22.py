booleano = True
som = 0
cont = 0
while booleano:
    nota = 10
    while 10 >= nota <= 20:
        nota = float(input("Digite a nota"))
        if nota > 20:
            break
        som += nota
        cont += 1
    if nota > 20:
        booleano = False
print('A média é', som/cont)
