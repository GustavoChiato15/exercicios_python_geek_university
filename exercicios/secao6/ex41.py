num = int(input("digite um número natural"))
term1 = 0
term2 = 1
print(term1,'->', term2,'-> ',end='')
for x in range(2, num):
    term3 = term1 + term2
    if term3 > num:
        print(term3, end='')
        break
    print(term3, end='')
    print(" -> " if x < num-1 else " Fim", end='')
    term1 = term2
    term2 = term3
print(" - FIM")