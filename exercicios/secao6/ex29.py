print("_" * 8)
print("Sequência de Fibonacci")
print("_" * 8)
som = 0
termos = int(input("Quantos termos você quer mostrar?"))
t1 = 0
t2 = 1
print('~'* 30)
print(f"{t1} -> {t2} ->", end='')
for x in range(3, termos+1):
    t3 = t1 + t2
    print(f" {t3} ", end= '')
    print("->" if x != termos else "FIM",end='')
    t1 = t2
    t2 = t3
