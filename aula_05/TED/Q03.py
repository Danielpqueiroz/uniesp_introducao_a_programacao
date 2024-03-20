# 3. Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
# a. o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
# b. o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;
import random
from random import randint

q = random.choices(range(0,100),k=20)
maior=0
menor=100
print(q)

for i in range(len(q)):
    if q[i]>maior:
        maior=q[i]
    if q[i]<menor:
        menor=q[i]

print(f"O maior valor da lista foi: {maior}")
print(f"O menor valor da lista foi: {menor}")