'''4. Faça um programa que receba um número e que calcule e mostre 
a tabuada desse número..
'''
num = int(input("Digite o numero da tabuada desejada:" ))
print("A seguir está a tabuada desejada:")
for num2 in range(1,11):
    resultado = num * num2
    print(f" {num} * {num2} = {resultado}")