produtos = {
    'banana': 2.50,
    'maça': 3.00,
    'laranja': 2.75,
    'abacaxi': 4.50,
    'manga': 3.50
}

print("O preço de uma maçã é: R$"+ str(produtos['maça']))


produtos['melancia'] = 6.00

for produtos, price in produtos.items():
    print(produtos + ": R$" + str(price))