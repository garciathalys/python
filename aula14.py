nome = 'Clara'
print('ara' in nome)
print(10 * '-')
print('laura' not in nome)


nome = input('Digite algum nome: ')
encontrar = input('Digite o que deseja encontrar:')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')