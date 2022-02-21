soma = 0
term1 = 0
term2 = 1
while True:
    term3 = term1 + term2
    if term3 > 4000000:
        break
    if term3 % 2 ==0:
        print(f"{term3} ->", end='')
        soma += term3
    term1 = term2
    term2 = term3
print(f"A soma desses números é \n{soma}")