import math
while True:
    num = float(input("Digite um valor:"))
    if num <= 0:
        print(":( " * 7)
        print("Finalizando programa")
        break
    print(f"quadrado de {num} = {num**2}\n raiz quadrada de {num} = {math.sqrt(num)}")
