cont, soma ,l_primos = 0, 0, []
a = int(input("Digite um número inteiro positivo a:"))
while a <= 0:
    a = int(input("Digite um número inteiro positivo a:"))
b = int(input("Digite um número inteiro positivo b:"))
while b <=0:
    b = int(input("Digite um número inteiro positivo b:"))
if a > b:
    c = b
    b = a
    a = c
if a or b == 2:
    print(2)
    l_primos.append(2)
    cont += 1
    soma += 2
for num in range(a, b+1):
    for n in range(2, num):
        if num % n == 0:
            break
        else:
            print(num)
            l_primos.append(num)
            cont += 1
            soma += num
            break
print(f"Os {cont} números primos detectados foram {l_primos}, cuja soma é {soma}")
