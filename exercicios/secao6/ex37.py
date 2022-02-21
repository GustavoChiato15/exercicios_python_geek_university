booleano = True
maior = 0
menor = 0
cont = 0
while booleano:
    num = int(input("Digite um número inteiro(num negativo para parar programa):"))
    if num < 0:
        if cont == 0:
            maior = "Não existe número maior"
            menor = "Não existe número menor"
        break
    else:
        if cont == 0:
            maior = num
            menor = num
            cont += 1
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
print("~" * 20, f"\n Maior: {maior}\n Menor: {menor}")