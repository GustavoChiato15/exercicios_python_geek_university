while True:
    print("""
    Digite 0 para finalizar o programa
    Digite 1 para converter km/h em m/s
    Digite 2 para converter m/s em km/h
    """)
    opcao = int(input("Digite a opção de sua escolha"))
    if opcao == 0:
        break
    if opcao == 1:
        km = float(input("Digite a quantidade de km/h a ser convertido:"))

        print(f"{km}km/h sendo convertido para m/s fica {km/3.6} m/s")
    if opcao == 2:
        ms = float(input("Digite a quantidade de m/s a ser convertido:"))

        print(f"{ms}m/s sendo convertido para km/h fica {ms*3.6} km/h")