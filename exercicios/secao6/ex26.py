num = int(input("Digite um número: "))
for x in range(1, num+1):
    if x % 11 == 0 or x % 13 == 0 or x % 17 == 0:
        print(x)