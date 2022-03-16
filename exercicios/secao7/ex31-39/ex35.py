lista_a, lista_b, lista_soma, cont, cont2 = [], [], [], 1, 0
a = int(input(f"Digite o {cont}º numero natural menor que 10000 : "))
while a < 0 or a >= 10000:
    a = int(input(f"Digite o {cont}º número natural menor que 10000 : "))
cont += 1
b = int(input(f"Digite o {cont}º número natural menor que 10000 : "))
while b < 0 or b >= 10000:
    b = int(input(f"Digite o {cont}º número natural menor que 10000:"))
string_a = str(a)
string_b = str(b)
for element in range(len(string_a)-1, -1, -1):
    lista_a.append(int(string_a[element]))
    #print(string_a[element])
print(lista_a)
for element in range(len(string_b)-1, -1, -1):
    lista_b.append(int(string_b[element]))
    #print(string_b[element])
print(lista_b)
while len(lista_a) < len(lista_b):
    lista_a.insert(len(lista_a), 0)
while len(lista_b) < len(lista_a):
    lista_b.insert(len(lista_b), 0)
while lista_a != [] and lista_b != []:
    lista_soma.append(lista_a[cont2] + lista_b[cont2])
    lista_a.pop(cont2)
    lista_b.pop(cont2)
    # print(lista_a)
    # print(lista_b)
#print(lista_soma)
lista_soma.reverse()
print(lista_soma)