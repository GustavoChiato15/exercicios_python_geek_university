for x in range(1000, 10000):
    string_x = str(x)
    x_inicial = int(string_x[0:2])
    x_final = int(string_x[2:4])
    som = x_inicial + x_final
    if som ** 2 == x:
        print(f"{x} possue soma de algorismos {som} e elevado a dois da ele mesmo")
