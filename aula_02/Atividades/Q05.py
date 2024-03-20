'''5. Utilizando a lista do exercício anterior, exiba uma saudação 
("Olá como vai você"), personalizado com o nome de cada amigo.
 A saudação deve ser a mesma, alterando apenas o nome do amigo.
'''
lista_amigos = ['Analicia','Luiz','Galvão Bueno']
for nome in lista_amigos:
    print(f"Olá, como vai você {nome}?")
#outro modo
lista_amigos = ['Analicia','Luiz','Galvão Bueno']
x = 0
while x < len(lista_amigos):
    print(f"Olá, como vai você {lista_amigos[x]}?")
    x +=1
