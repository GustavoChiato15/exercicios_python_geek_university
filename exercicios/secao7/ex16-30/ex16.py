cont, lista = 1, []
while cont <= 5:
    num = float(input(f"Digite o {cont} numero a ser adicionado na lista:\n"))
    lista.append(num)
    cont += 1
while True:
    codigo = int(input("""
    0. Sair
    1. Mostrar Lista
    2. Mostrar Lista Invertida
    
    Digite a opcao desejada: """))
    if codigo == 0:
        break
    elif codigo == 1:
        print(f"A lista é {lista}")
    elif codigo == 2:
        print(f"A lista invertida é {lista[::-1]}")
    else:
        print("Código Inválido")
