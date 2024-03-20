# Atividade Avaliativa - Questão 1
controle = True
while controle:
    sair= (input('Digite S para sair ou C para continuar:')).upper()

    if sair=="S":
        controle= False
    else:

        A = float(input("Digite o valor de A da equação Ax^2 + Bx + C: "))
        B = float(input("Digite o valor de B da equação Ax^2 + Bx + C: "))
        C = float(input("Digite o valor de C da equação Ax^2 + Bx + C: "))

        delta =((B**2) - (4 * A * C)) 

        if delta > 0:
            bask1 = ((-B + (pow(delta,0.5)))/(2*A))
            bask2 = ((-B - (pow(delta,0.5)))/(2*A))

            print(f"O primeiro valor da raiz é : {bask1}")
            print(f"O segundo valor da raiz é : {bask2}")
        else:
            print("Digite um número menor para A e C")

# Atividade Avaliativa - Questão 2
controle = True
while controle:
    sair= (input('Digite S para sair ou C para continuar:')).upper()

    if sair=="S":
        controle= False
    else:
        x1 = float(input("Digite o valor de (x) do primeiro ponto ex: (P(x,y)): "))
        y1 = float(input("Digite o valor de (y) do primeiro ponto ex: (P(x,y)): "))
        x2 = float(input("Digite o valor de (x) do segundo ponto ex: (Q(x,y)): "))
        y2 = float(input("Digite o valor de (y) do segundo ponto ex: (Q(x,y)): "))

        z = (((x2-x1)**2)+((y2-y1)**2))
        d = (pow(z,0.5))

        print(f" A distancia entre os pontos é: {d}")

# Atividade Avaliativa - Questão 3


operacao = True
while operacao:
    print("Caso você queira fazer uma operação de adição entre os números digite: 1")
    print("Caso você queira fazer uma subtração de adição entre os números digite: 2")
    print("Caso você queira fazer uma multiplicação de adição entre os números digite: 3")
    print("Caso você queira fazer uma divisão de adição entre os números digite: 4")
    print("Caso você queira fazer uma potenciação de adição entre os números digite: 5")
    print("Digite 0 para sair")
    operacao = int(input("Digite a opção desejada: "))

    if operacao == 0 :
        operacao = False
    else:

        num1 = float(input("Digite um número : "))
        num2 = float(input("Digite outro número : "))

        x = 0

        match operacao:
            case 1:
                x = num1+num2
                print(f"O resultado da adição entre os numeros é : {x}")
            case 2:
                x = num1-num2
                print(f"O resultado da adição entre os numeros é : {x}")
            case 3:
                x = num1*num2
                print(f"O resultado da adição entre os numeros é : {x}")
            case 4:
                x = num1/num2
                print(f"O resultado da adição entre os numeros é : {x}")
            case 5:
                x = num1**num2
                print(f"O resultado da adição entre os numeros é : {x}")
    
            
# Atividade Avaliativa - Questão 4
controle = True
while controle:
    sair= (input('Digite S para sair ou C para continuar:')).upper()

    if sair=="S":
        controle= False
    else:
        peso = float(input("Informe seu peso: "))
        altura = float(input("Informe sua altura: "))
        imc = (peso/(altura**2))

        if 0 < imc < 18.5:
            print(f"Seu IMC é : {imc:.2f} e você está abaixo do peso")
        elif 18.5 <= imc < 25:
            print(f"Seu IMC é : {imc:.2f} e você está com peso normal")
        elif 25 <= imc < 30:
            print(f"Seu IMC é : {imc:.2f} e você está com peso normal")
        else:
            print(f"Seu IMC é : {imc:.2f} e você está obeso")

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

# Atividade Avaliativa - Questão 6



controle = True
while controle:
    sair= (input('Digite S para sair ou C para continuar:')).upper()

    if sair=="S":
        controle= False
    else:
        num = int(input("Digite um número para ser calculado seu fatorial: "))
        
        resultado=1
        count=1

        while count <= num:
            resultado *= count
            count += 1
            print(f" {resultado}", end=" x")
           
        print(f" = {resultado}")