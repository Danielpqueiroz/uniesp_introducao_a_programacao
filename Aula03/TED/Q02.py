'''Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).'''
ano = int(input("Digite o ano atual: "))
ano_nasc = int(input("Digite o ano do seu nascimento: "))
votar = ano - ano_nasc
if votar >= 16:
    print("Parabens se vc estiver com seu titulo eleitoral em dia você poderá votar este ano!")
else:
    print("Infelismente você ainda não pode votar. ")