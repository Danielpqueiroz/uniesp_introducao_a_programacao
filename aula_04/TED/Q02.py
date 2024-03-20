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