cadastro = {}

while True:
    nome = input("Digite seu nome: ")
    if nome == '':
        break
    
    idade = int(input("Dgite sua idade: "))
    cidade = input("Digite sua cidade: ")
    
    cadastro[nome] = {"Idade": idade, "Cidade": cidade}
    
print("Cadastro:")
print(cadastro)

for nome, dados in cadastro.items():
    print("- Nome", nome)
    print("- Idade", dados['Idade'])
    print("- cidade", dados['Cidade'])
