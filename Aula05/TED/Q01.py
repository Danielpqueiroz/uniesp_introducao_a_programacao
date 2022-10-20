# 1. Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes
# lidos em um vetor (lista). Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de
# clube e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente
# (guardados no vetor), ou NÃO ACHEI caso contrário.
import random
matriz = ["Palmeiras", "Flamengo", "Corintias", "Botafogo", "Fluminense", "Fortaleza", "Goiás", "Juventude", "Internacional","Avaí", "America", "Atletico", "Santos"]
clubes =[]

clubes = random.sample(matriz, 10)
print(clubes)
nome = random.choice(matriz)
print(nome)

x=False
for i in range(len(clubes)):
    
    if nome == clubes[i]:
        print(f"ACHEI, infelizmente o clube {clubes[i]} ja foi digitado anteriormente")
        x=True
    elif i == (len(clubes)-1) and x==False:
       print(f"NÃO ACHEI, o clube {nome} foi cadastrado com sucesso.")
