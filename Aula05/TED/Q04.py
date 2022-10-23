# 4. Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável X. Armazenar
# em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o
# vetor M.
import random
from random import randint

vetA = random.choices(range(0,100),k=10)
vetM = []
x = random.choice(range(0,100))
print(f"Vetor A: {vetA}")
print(f"O valor da variavel X foi: {x}")

for i in range(len(vetA)):
    vetM.append( vetA[i]*x)
print(f"Vetor M: {vetM}")
