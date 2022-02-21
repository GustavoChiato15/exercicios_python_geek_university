som = 0
qsom = 0
for x in range(1, 101):
    som += x**2
    qsom += x
qsom = qsom ** 2
result = qsom - som
print(f"A diferença entre quadrado da soma e soma dos quadrados é:\n{qsom} - {som} =  {result}")
