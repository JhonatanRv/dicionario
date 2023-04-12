votos = {}

while True:
    candidato = input("Digite o nome do seu candidato: ")
    if candidato ==  "fim":
        break
    
    if candidato in votos:
        votos[candidato] += 1
    else:
        votos[candidato] = 1
        
print("Resultado da votação: ")
for candidato, quantidade in votos.items():
    print(candidato, "-", quantidade, "votos")
    
print(votos)