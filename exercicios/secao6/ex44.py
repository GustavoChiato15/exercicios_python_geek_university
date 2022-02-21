from time import sleep
cont = 0
while True:
    if cont > 0:
        sleep(4)
    print("""
    Digite 1 para -> Adição
    Digite 2 para -> Subtração
    Digite 3 para -> Multiplicação
    Digite 4 para -> Divisão
    Digite 5 para -> Fechar programa
    """)
    cont = 1
    opcao = int(input("Digite sua opção:"))
    if opcao == 5:
        print("Finalizando programa...")
        print("(3)")
        sleep(1)
        print("(2)")
        sleep(1)
        print("(1)")
        sleep(1)
        break
    n = float(input("Digite um número"))
    n2 = float(input("Digite outro número"))
    if opcao == 1:
        print(f"A soma entre {n} e {n2} é {n+n2}")
    if opcao == 2:
        print(f"A subtração entrev{n} e {n2} é {n-n2}")
    if opcao == 3:
        print(f"A multiplicação entre {n} e {n2} é {n*n2}")
    if opcao == 4:
        print(f"A divisão entre {n} e {n2} é {n/n2}")
