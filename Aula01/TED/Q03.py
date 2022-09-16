'''As maçãs custam 1,30 cada, se forem compradas menos de 
uma dúzia, e 1,00 se forem compradas pelo menos 12. Escreva
 um programa que leia o número de maçãs compradas, calcule 
 e escreva o custo total da compra.'''
num = int(input("Digite a quantidade de maçãs desejada :"))
if 0 < num < 12:
    valor = num * 1.3
    print(f"O valor das {num} maçãs custam: R$ {valor}")
elif num >= 12:
    valor = num * 1
    print(f"O valor das {num} maçãs custam: R$ {valor}")
