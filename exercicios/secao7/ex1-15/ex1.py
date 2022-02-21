soma = 0
vetor_a = [1, 0, 5, -2, -5, 7]
soma += vetor_a[0] + vetor_a[1] + vetor_a[5]
print(f"A soma dos vetores {vetor_a[0]}, {vetor_a[1]}, {vetor_a[5]} é {soma}")
vetor_a.pop(4)
vetor_a.insert(4, 100)
for element in vetor_a:
    print(element)