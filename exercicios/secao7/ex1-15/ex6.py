cont, lista = 1, []
while cont <= 10:
    num = int(input(f"Digite o {cont}º número para ser inserido na lista:"))
    lista.append(num) # adiciona o número lido à lista
    cont += 1
print(f"""
O maior número lido foi o {max(lista)}
O menor número lido foi o {min(lista)}""")
