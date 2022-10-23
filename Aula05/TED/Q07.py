# 7. Faça um algoritmo para ler dois vetores V1 e V2 de 10 números cada. Calcular e escrever a
# quantidade de vezes que V1 e V2 possuem os mesmos números e nas mesmas posições.

import random
vetor1 = random.choices(range(1,10),k=30)
vetor2 = random.choices(range(1,10),k=30)
print(f"Vetor 1 = {vetor1}")
print(f"Vetor 2 = {vetor2}")

for i in range(len(vetor1)):
    if vetor1[i] == vetor2[i]:
        print(f"O número {vetor1[i]} repetiu nos dois vetores na posição {i}")

