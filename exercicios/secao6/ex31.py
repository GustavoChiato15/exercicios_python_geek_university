num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))
n = int(input("Quantos multiplos deseja mostrar?"))
nat_list, x = [], 0
while len(nat_list) < n:
    if x % num1 == 0 or x % num2 == 0:
        nat_list.append(x)
    x += 1
print(nat_list)