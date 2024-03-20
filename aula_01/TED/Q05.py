'''Ler dois valores (considere que não serão lidos valores
 iguais) e escrever o maior deles.'''
num01 = float(input("Digite o primeiro valor: "))
num02 = float(input("Digite o segundo valor: "))
if num01 != num02:
    if num01 > num02:
        print(f"O primeiro valor é maior do que o segundo valor digitado.")
    else:
        print(f"O segundo valor é maior do que o primeiro valor digitado.")

else:
    print(f"Os valores digitados são iguais.")
