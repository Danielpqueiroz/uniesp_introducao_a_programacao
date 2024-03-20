# with open("ATV.txt","r",encoding="utf-8") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# with open("ATV.txt","r",encoding="utf-8") as arquivo:
#     x = 0
#     for linha in arquivo:
#         print(f"Linha: {x} Conteudo: {linha}")
#         x = x + 1

# arquivo_de_linhas = []

# with open("ATV.txt","r",encoding="utf-8") as arquivo:
#     arquivo_de_linhas = arquivo.readlines()

# print(arquivo_de_linhas)

# for linha in arquivo_de_linhas:
#     conteudo_linha = linha.split(":")
#     print(conteudo_linha)

with open("arquivo_da_aula.txt","w",encoding="utf-8") as arquivo:
    arquivo.write("Testando uma escrita")

nome = "Daniel"

with open("arquivo_da_aula.txt","a",encoding="utf-8") as arquivo:
    for line in range(10):
        arquivo.write(f"{line} - Meu nome é {nome}\n")