lista_x, matriz, posicao_x = [], [], {}
cont = 1
x = int(input("Digite um valor que será encontrado na matriz:"))
for line in range(1, 6):
    linha_atual = []
    for colun in range(1, 6):
        valor = int(input(f"Digite o valor da linha {line} e coluna {colun}:"))
        if valor == x and cont == 1:
            posicao_x.update({"linha": line, "coluna": colun})
            lista_x.append(f"{cont}ªocorrencia de {x} na linha {posicao_x['linha']} e na coluna {posicao_x['coluna']}")
            cont += 1
        elif valor == x and cont != 1:
            posicao_x.update({"linha": line, "coluna": colun})
            lista_x.append(f"{cont}ª ocorrencia de {x} na linha {posicao_x['linha']} e na coluna {posicao_x['coluna']}")
            cont += 1
        linha_atual.append(valor)
    matriz.append(linha_atual)
for num in range(0, 5):
    print(matriz[num])
print(len(lista_x))
if len(lista_x) == 1:
    print(f'O valor {x} está localizado na matriz na linha {posicao_x.get("linha")} e coluna {posicao_x.get("coluna")}')
else:
    for element in lista_x:
        print(element)
