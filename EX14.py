estudantes = {
    "João": {
        'Idade': 18,
        'Cidade': 'São Paulo',
        'Notas': [7.5, 8.0, 9.0]
    },
    "Maria": {
        'Idade': 20,
        'Cidade': 'Rio de Janeiro',
        'Notas': [6.5, 7.0, 8.5]
    },
    "Pedro": {
        'Idade': 19,
        'Cidade': 'Belo Horizonte',
        'Notas': [8.0, 8.5, 9.5]
    },
}

print("A idade de joão é: " + str(estudantes['João']['Idade']))

estudantes['Maria']['Notas'].append(9.0)

for estudantes, info in estudantes.items():
    print(estudantes + ':')
    print('Idade: ' + str(info['Idade']))
    print('Idade: ' + info['Cidade'])
    print('Idade: ' + str(info['Notas']))
    print('Idade: ' + str(sum(info['Notas']) / len(info['Notas'])))