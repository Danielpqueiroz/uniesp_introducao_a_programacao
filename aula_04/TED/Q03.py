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
    
            