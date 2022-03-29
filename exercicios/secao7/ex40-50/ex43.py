matriz, local_maiores = [], []
cont, maior, local_maior, qtd_maior= 0, None, {}, 1
for line in range(1, 5):
    linha = []
    for colun in range(1, 5):
        elemento_matriz = int(input(f"Digite o valor da linha {line} e da coluna {colun} da matriz"))
        if cont == 0:
            maior = elemento_matriz
            local_maior.update({'linha': line, 'coluna': colun})
            cont += 1
        else:
            if elemento_matriz == maior:
                qtd_maior += 1
                local_maiores.append({'valor': elemento_matriz, 'linha': line, 'coluna': colun})
            if elemento_matriz > maior:
                qtd_maior = 1
                local_maior.clear()
                local_maiores.clear()
                local_maiores.append({'valor': elemento_matriz, 'linha': line, 'coluna': colun})
                maior = elemento_matriz
                local_maior.update({'linha': line, 'coluna': colun})
        linha.append(elemento_matriz)
    matriz.append(linha)
for num in range(0, 4):
    print(matriz[num])

if qtd_maior == 1:
    print(f"O maior valor da matriz é {maior} e está localizado na linha {local_maior['linha']} e na coluna {local_maior['coluna']}")
else:
    print(f"Foram encontrados {qtd_maior} números considerados como maiores e estão localizados respectivamente em: ")
    for element in range(qtd_maior):
        print(local_maiores[element])
