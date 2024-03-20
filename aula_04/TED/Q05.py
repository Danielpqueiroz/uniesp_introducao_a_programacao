# Atividade Avaliativa - Questão 5

num = 0
num0_25 = 0
num26_50 = 0
num51_75 = 0
num76_100 = 0
cont = 0

while num >=0:
    num = float(input("Digite um numero: "))

    if num <=0:
        num = num
    else:
        if 0<=num<=25:
            num0_25 += 1 
        elif 26<=num<=50:
            num26_50 += 1 

        elif 51<=num<=75:
            num51_75 += 1 

        elif 76<=num<=100:
            num76_100 += 1 
        cont += 1
        print(f"A quntidade de numeros digitados é : {cont}")
        print(f"A quantidade de numeros entre 0 e 25 é : {num0_25}")
        print(f"A quantidade de numeros entre 26 e 50 é : {num26_50}")
        print(f"A quantidade de numeros entre 51 e 75 é : {num51_75}")
        print(f"A quantidade de numeros entre 76 e 25 é : {num76_100}")