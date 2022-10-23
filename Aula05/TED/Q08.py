# 8. Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer,
# calcular e escrever quantas vezes esse número aparece no vetor
from random import randint
import random

vetor = random.choices(range(1,10),k=30)
print(f"O vetor é: {vetor}")

vetor.append(randint(0,5))
print(f"Um número foi adicionado na posição 30 do vetor: {vetor}")

x=0
for i in range(len(vetor)):
    if vetor[30] == vetor[i]:
        x = x+1
print(f"O número {vetor[30]} que você digitou repetiu {x} veze(s) no vetor.")
