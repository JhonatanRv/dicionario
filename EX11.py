agenda= {}

while True:
    nome = input("Digite seu nome: ")
    if nome ==  "":
        break
    
    telefone = input("Digite seu número: ")
    agenda[nome] = telefone
    
    
nome_pesquisa = input("digite o nome para pesquisar: ")
if nome_pesquisa in agenda:
    print("Telefone de: ",nome_pesquisa, ":", agenda[nome_pesquisa])
else:
    print("Nome não econtrado na agenda")