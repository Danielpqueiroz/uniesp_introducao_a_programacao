'''3. Armazene os nomes de alguns de seus amigos em uma lista 
chamada amigos. Exiba o nome de cada
pessoa acessando cada elemento da lista um de cada vez.
'''
lista_amigos = ['Analicia','Luiz','Galvão Bueno']
for nome in lista_amigos:
    print(f"{nome}, obrigado por vir a aula!")
#outro modo
lista_amigos = ['Analicia','Luiz','Galvão Bueno']
x = 0
while x < len(lista_amigos):
    print(f"{lista_amigos[x]}, obrigado por vir!")
    x +=1
