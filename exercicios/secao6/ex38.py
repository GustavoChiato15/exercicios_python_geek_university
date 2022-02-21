print("-="*20)
while True:
    r1 = float(input("Digite o valor da primeira resistência:"))
    if r1 != 0:
        print('Okay')
    else:
        print(",_, " * 10)
        print("Encerrando programa número nulo recebido")
        break
    r2 = float(input("Digite o valor da primeira resistência:"))
    if r2 != 0:
        print("Okay")
    else:
        print(";-; " * 10)
        print("Encerrando programa número nulo recebido")
        break
    print((r1*r2)/(r1+r2))
