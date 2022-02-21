cont = 0
lista = []
for x in range(0, 101):
    if x % 3 == 0 and x > 0:
        if cont <= 4:
            lista.append(x)
            cont += 1
        else:
            break
print(f"Os 5 primeiros números múltiplos de 3 são {lista}")
