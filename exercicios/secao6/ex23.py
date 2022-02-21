n = int(input("Digite um número:"))
for x in range(1, n+1):
    if n % x == 0:
        print(f"Divisores:{x}")