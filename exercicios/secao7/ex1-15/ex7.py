cont, lista_int = 1, []
while cont <= 10:
    num = int(input(f"Digite o {cont}º número que será inserido na lista:\n"))
    lista_int.append(num)
    cont += 1
maior_numero = max(lista_int)
print(f"""
A lista é essa: {lista_int}
O maior número é esse: {maior_numero}
O maior número está localizado nesse index: {lista_int.index(maior_numero)}""")