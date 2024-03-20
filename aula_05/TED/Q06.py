# 6. Faça um algoritmo para ler um vetor de 20 números. Após isto, deverá ser lido mais um número
# qualquer e verificar se esse número existe no vetor ou não. Se existir, o algoritmo deve gerar um novo
# vetor sem esse número. (Considere que não haverão números repetidos no vetor).

import random
from random import randint

num = random.sample(range(1,21),20)
print(num)
num.append(randint(0,5))
print(f"O número escolhido foi o da posição 20: {num}")
num2=-1
for i in range(len(num)-1):
    if num[20] == num[i]:
        num2 = i

if num2>-1:        
    print(f"O número {num[num2]} foi excluido da posição {num2}.")
    del num[num2]       
print(f"O vetor atualizado é:  {num}")



