from time import sleep
cont, soma, num = 0, 0, 2
verdadeiro = True
while verdadeiro:
    primo = True
    for n in range(2, num):
        if num % n == 0:
            primo = False
            break
    if primo:
        cont += 1
        print(f'{cont}ºprimo é {num}')
        sleep(1)
        soma += num
    num += 1
    if num == 1999999:
        verdadeiro = False
print(f'A soma de todos os números primos é {soma}')
