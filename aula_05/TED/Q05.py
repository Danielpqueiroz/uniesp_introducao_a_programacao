# 5. Crie um vetor N que seja resultado da soma dos itens de outros dois vetores A e B. Exemplo: A[0] +
# B[0] deverá ser salva em N[0].
import random
from random import randint

vetA = random.choices(range(0,100),k=10)
vetB = random.choices(range(0,100),k=10)
vetN = []

for i in range(len(vetA)):
    vetN.append(vetA[i]+vetB[i])

print(f"Vetor A: {vetA}")
print(f"Vetor B: {vetB}")
print(f"Vetor N: {vetN}")