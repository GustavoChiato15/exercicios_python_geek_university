saque = int(input("Digite o saque necessário nessa operação:"))
cedula = 100
notas = 0
while True:
    if saque >= cedula:
        saque -= cedula
        notas += 1
    else:
        print(f"Total de {notas} notas de R${cedula}")
        notas = 0
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        if saque == 0:
            break
