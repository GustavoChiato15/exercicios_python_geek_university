from time import sleep
chico_alt = 1.50
ze_alt = 1.10
ano = 0
while True:
    if ze_alt > chico_alt:
        print(f"A altura de zé ficou maior que a de Carlos em {ano} anos")
        break
    ano += 1
    chico_alt += 0.02
    ze_alt += 0.03
    print(f"Altura de chico no {ano}º ano = {chico_alt:.2f}")
    print(f"Altura de ze no {ano}º ano = {ze_alt:.2f}")
    sleep(3)
