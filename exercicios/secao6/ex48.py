from time import sleep
salario = 2000
aumento = 0.75
ano = 1996
for x in range(1996, 2022):
    aumento += aumento
    print(f" O salário do funcionario recebeu um aumento de {aumento}% em {ano}" if aumento == 1.5 else
          f"O salário do funcionario recebeu um aumento de {int(aumento)}% em {ano}")
    salario = salario + salario*(aumento/100)
    print(f"Salario: {salario:.2f}R$")
    ano += 1
    sleep(2)
