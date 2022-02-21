intervalo_inicial = int(input("Digite o intervalo inicial:"))
intervalo_final = int(input("Digite o intervalo final:"))
som = 0
for x in range(intervalo_inicial, intervalo_final+1):
    if x % 2 == 1:
        som += x
print(f"Soma dos ímpares neste intervalo: {som}")
