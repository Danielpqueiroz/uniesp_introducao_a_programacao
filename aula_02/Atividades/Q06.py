'''6. Seja criativo ao desenvolver este programa.
a. Crie uma lista de convidados para um jantar em sua casa,
 com pelo menos 5 celebridades.
b. Envie um convite para cada uma dessas pessoas. Com a
 mesma mensagem e nome personalizado.
c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar,
 você deverá enviar novos convites. Imprima o nome das pessoas
 que não poderão comparecer.
d. Modifique sua lista, substitua os desistentes por novos convidados.
e. Exiba um novo convite para cada pessoa que continua presente
 em sua lista.
'''
import random
lista_amigos = ['Elon Musk','Nicolas Tesla','Thomas Edison','Messias','Juliete']
lista_amigos_secundarios = ['Gisele Bündchen','Ivete Sangalo']
x = 0
while x < len(lista_amigos):
    print(f"Olá, {lista_amigos[x]} você esta convidado(a) para minha festa!")
    x +=1
y = random.randrange(0,len(lista_amigos))
#print(y)
print(f"Olá, {lista_amigos[y]} reforçando que você esta convidado(a) para minha festa!")
print(f"O {lista_amigos[y]} não poderá comparecer a festa.")
z = random.randrange(1,len(lista_amigos_secundarios))
lista_amigos[y] = lista_amigos_secundarios[z]
x = 0
while x < len(lista_amigos):
    print(f"Olá, {lista_amigos[x]} você esta convidado(a) para minha festa!")
    x +=1