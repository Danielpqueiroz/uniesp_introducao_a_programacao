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
        