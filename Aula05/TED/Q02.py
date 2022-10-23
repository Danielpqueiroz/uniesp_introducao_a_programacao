# 2. Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. Calcular a média da
# turma e contar quantos alunos obtiveram nota acima desta média calculada. Escrever a média da
# turma e o resultado da contagem.
import random
from random import randint

notas = random.choices(range(0,10),k=20)
print(notas)
soma=0
acima=0

for i in range(len(notas)):
    soma = soma + notas[i]

media= soma/len(notas)
print(f"A media da turma foi: {media}")

for j in range(len(notas)):
    if notas[j]> media:
        acima=acima+1

print(f"Essa foi a quantidade de aluno que tiraram notas acima da media: {acima}")
