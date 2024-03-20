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