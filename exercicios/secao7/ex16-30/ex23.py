from time import sleep
produto_escalar, cont, lista_rs_1, lista_rs_2 = 0, 1, [], []
while cont <= 5:
    num = float(input(f"Digite o {cont}º número real da lista 1:"))
    lista_rs_1.append(num)
    cont += 1
cont = 1
while cont <= 5:
    num = float(input(f"Digite o {cont}º número real da lista 2:"))
    lista_rs_2.append(num)
    cont += 1
for n in range(0, 5):
    produto_escalar += lista_rs_1[n] * lista_rs_2[n]
    print(f"{lista_rs_1[n]} * {lista_rs_2[n]} = {lista_rs_1[n] * lista_rs_2[n]}")
    sleep(1)
print(f"O resultado total é {produto_escalar}")
