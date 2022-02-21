som, peso, cont, lista = 0, 0, 1, []
while cont <= 5:
    num = int(input(f"Digite o {cont}º número à ser adicionado na lista"))
    lista.append(num)
    cont += 1
for element in lista:
    som += element
    peso += 1
print(f"""
A soma dos {cont} números é {som}
A média dos {cont} números é {som/peso}
O maior número é {max(lista)}
O menor número é {min(lista)}
""")



