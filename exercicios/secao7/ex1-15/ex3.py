list_float = []
list_float_sqr = []
for x in range(1, 11):
    num_float = float(input("Digite um número real"))
    list_float.append(num_float)
    list_float_sqr.append(num_float**2)
print(f"A lista normal é: {list_float}")
print(f"A lista com termos ao quadrado é:", end='')
for element in list_float_sqr:
    print(f"{element:.2f} -= ", end='')
