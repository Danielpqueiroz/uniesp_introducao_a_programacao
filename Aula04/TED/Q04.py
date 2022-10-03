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