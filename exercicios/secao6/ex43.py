from random import randint
n = randint(1, 1000)
while True:
    chute = int(input("Adivinhe o número gerado"))
    if chute == n:
        print("Parabéns lixo você acertou! :)")
        break
    if chute > n:
        print("Seu chute foi maior que o número gerado")
    else:
        print("Seu chute foi menor que o número gerado")