'''Ler as notas da 1a. e 2a. avaliações de um aluno.
 Calcular a média aritmética simples e escrever uma 
 mensagem que diga se o aluno foi ou não aprovado 
 (considerar que nota igual ou maior que 6 o aluno é aprovado).
  Escrever também a média calculada.'''
nota01 = float(input("Digite o valor da nota da sua primeira avaliação: "))
nota02 = float(input("Digite o valor da nota da sua segunda avaliação:"))
media = (nota01+nota02)/2
if 10 >= media >= 6:
    print(f"Parabéns você foi aprovado com media {media}.")
elif 0 <= media < 6:
    print(f"Você foi reprovado.")
