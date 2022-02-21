from random import randint
vezes = int(input("Digite o número de vezes a rodar o programa:"))
for x in range(1, vezes+1):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print(f"{x}ª rodada")
    print(f"primeiro dado:{d1}\n segundo dado:{d2}")
    print(f"primeiro dado é maior que segundo"if d1 > d2 else "")
    print(f"segundo dado é maior que primeiro" if d2 > d1 else "")
    print("Os números são iguais" if d1 == d2 else "")