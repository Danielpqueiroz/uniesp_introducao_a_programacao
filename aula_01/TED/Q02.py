'''Solicite ao usuário um valor numérico, inteiro ou real, 
e escrever se é positivo ou negativo (considere o valor 
zero como positivo).'''
num = float(input("Digite um número :"))
if num > -1:
    print(f"O número {num} é POSITIVO")
else:
    print(f"O número {num} é NEGATIVO")
