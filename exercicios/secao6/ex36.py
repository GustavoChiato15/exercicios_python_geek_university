base = 0
altura = 0
while base <= 0 or altura <= 0:
    base = float(input("Digite a base da área:"))
    altura = float(input("Digite a altura:"))
print(f"A área é {base*altura:.2f}m")
