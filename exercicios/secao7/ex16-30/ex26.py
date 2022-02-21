from math import sqrt
cont, lista_n, soma_n, peso_n, media_n, soma_n_c_media, peso_n_c_media = 1, [], 0, 0, 0, 0, 0
while cont <= 3:
    n = float(input(f"Digite o {cont}º numero para ser adicionado na somatória do desvio padrão"))
    lista_n.append(n)
    cont += 1
for element in lista_n:
    soma_n += element
    peso_n += 1
media_n = soma_n/peso_n
print(media_n)
for element in lista_n:
    element = (element - media_n) ** 2
    soma_n_c_media += element
    peso_n_c_media += 1
dp = sqrt(soma_n_c_media/peso_n_c_media)
print(dp)
