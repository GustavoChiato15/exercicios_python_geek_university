from time import sleep
meses = 0
carlos = float(input("Digite o salário de Carlos sendo que o de joao será 1/3 dele:"))
joao = carlos / 3
while True:
    sleep(3)
    if joao > carlos:
        print(f"Salário de joão ultrapassou o de Carlos em {meses} meses")
        break
    joao = joao + joao * (5/100)
    meses += 1
    print(f"Salario joao no  mes {meses}  = {joao:.2f}R$")
    carlos = carlos + carlos * (2/100)
    print(f"Salário Carlos no mes {meses} = {carlos:.2f}R$")
