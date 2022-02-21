from time import sleep
habitantes = int(input("Digite o número de habitantes da região:"))
valor_kwh = float(input("Digite o valor do kwh para cada habitante: R$"))
cont = 1
media = 0
consumo_residencial, consumo_comercial, consumo_industrial = 0, 0, 0
cont_maior = "nenhum"
cont_menor = "nenhum"
maior = True
menor = True
for pessoa in range(1, habitantes+1):
    consumo = float(input(f"Quantos kwh foram gastos pelo {cont} habitante? :"))
    media += consumo
    if cont == 1:
        maior = consumo
        cont_menor, cont_maior = cont, cont
        menor = consumo
    if consumo > maior:
        maior = consumo
        cont_maior = cont
    elif consumo < menor:
        menor = consumo
        cont_menor = cont
    cont += 1
    codigo_consumidor = int(input(
        """Digite o código do consumidor
        1 - Residencial
        2 - Comercial
        3 - Industrial
        """))
    if codigo_consumidor == 1:
        consumo_residencial += consumo
    elif codigo_consumidor == 2:
        consumo_comercial += consumo
    elif codigo_consumidor == 3:
        consumo_industrial += consumo
sleep(1)
print(f"""Maior consumo de energia:
        Designado ao {cont_maior}º habitante que gastou {maior}kwh
        totalizando R$ {maior*valor_kwh:.2f}.""")
sleep(1)
print(f"""Menor consumo de energia:
    Designado ao {cont_menor}º habitante que gastou {menor}kwh
    totalizando R$ {menor*valor_kwh:.2f}""")
sleep(1)
print(f"""A média de consumo dos habitantes é {media/habitantes:.2f}kwh""")
sleep(1)
print(f"""
O consumo residencial é de {consumo_residencial}kwh
O consumo comercial é de {consumo_comercial}kwh
O consumo industrial é de {consumo_industrial}kwh
""")
