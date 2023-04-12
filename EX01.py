dicionario = {"gato": "chat", "dog": "chien", "cavalo": "cheval"}
palavras = ["gato", "lion", ]

for palavra in palavras:
    if palavra in dicionario:
        print(palavra,"->", dicionario[palavra])
    else:
        print(palavra, "Não está no dicionário")